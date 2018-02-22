// Copyright (c) 2017 Zededa, Inc.
// All rights reserved.

package main

import (
	"bytes"
	"crypto/sha256"
	"crypto/tls"
	"crypto/x509"
	"fmt"
	"github.com/golang/protobuf/proto"
	"github.com/zededa/api/zconfig"
	"github.com/zededa/go-provision/types"
	"golang.org/x/crypto/ocsp"
	"io/ioutil"
	"log"
	"mime"
	"net"
	"net/http"
	"net/http/httptrace"
	"os"
	"strings"
	"time"
)

const (
	MaxReaderSmall      = 1 << 16 // 64k
	MaxReaderMaxDefault = MaxReaderSmall
	MaxReaderMedium     = 1 << 19 // 512k
	MaxReaderHuge       = 1 << 21 // two megabytes
	configTickTimeout   = 1       // in minutes
)

var configApi string = "api/v1/edgedevice/config"
var statusApi string = "api/v1/edgedevice/info"
var metricsApi string = "api/v1/edgedevice/metrics"

// XXX remove global variables
// XXX shouldn't we know our own device UUID? Get from some global struct?
// Or read from uuid file?
var deviceId string

// These URLs are effectively constants; depends on the server name
var configUrl string
var metricsUrl string
var statusUrl string

const (
	identityDirname = "/config"
	serverFilename  = identityDirname + "/server"
	deviceCertName  = identityDirname + "/device.cert.pem"
	deviceKeyName   = identityDirname + "/device.key.pem"
	rootCertName    = identityDirname + "/root-certificate.pem"
)

// tlsConfig is initialized once i.e. effectively a constant
var tlsConfig *tls.Config

func getCloudUrls() {

	// get the server name
	bytes, err := ioutil.ReadFile(serverFilename)
	if err != nil {
		log.Fatal(err)
	}
	strTrim := strings.TrimSpace(string(bytes))
	serverName := strings.Split(strTrim, ":")[0]

	configUrl = serverName + "/" + configApi
	statusUrl = serverName + "/" + statusApi
	metricsUrl = serverName + "/" + metricsApi

	deviceCert, err := tls.LoadX509KeyPair(deviceCertName, deviceKeyName)
	if err != nil {
		log.Fatal(err)
	}
	// Load CA cert
	caCert, err := ioutil.ReadFile(rootCertName)
	if err != nil {
		log.Fatal(err)
	}
	caCertPool := x509.NewCertPool()
	caCertPool.AppendCertsFromPEM(caCert)

	tlsConfig = &tls.Config{
		Certificates: []tls.Certificate{deviceCert},
		ServerName:   serverName,
		RootCAs:      caCertPool,
		CipherSuites: []uint16{
			tls.TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384,
			tls.TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256},
		// TLS 1.2 because we can
		MinVersion: tls.VersionTLS12,
	}
	tlsConfig.BuildNameToCertificate()
}

// got a trigger for new config. check the present version and compare
// if this is a new version, initiate update
//  compare the old version config with the new one
// delete if some thing is not present in the old config
// for the new config create entries in the zMgerConfig Dir
// for each of the above buckets
// XXX should the timers be randomized to avoid self-synchronization across
// potentially lots of devices?
// Combine with being able to change the timer intervals - generate at random
// times between .3x and 1x
func configTimerTask() {
	iteration := 0
	getLatestConfig(configUrl, iteration)

	ticker := time.NewTicker(time.Minute * configTickTimeout)

	for range ticker.C {
		iteration += 1
		getLatestConfig(configUrl, iteration)
	}
}

// Each iteration we try a different uplink. For each uplink we try all
// its local IP addresses until we get a success.
func getLatestConfig(configUrl string, iteration int) {
	intf, err := types.GetUplinkAny(deviceNetworkStatus, iteration)
	if err != nil {
		log.Printf("getLatestConfig: %s\n", err)
		return
	}
	addrCount := types.CountLocalAddrAny(deviceNetworkStatus, intf)
	if debug {
		log.Printf("Connecting to %s using intf %s interation %d #sources %d\n",
			configUrl, intf, iteration, addrCount)
	}
	for retryCount := 0; retryCount < addrCount; retryCount += 1 {
		localAddr, err := types.GetLocalAddrAny(deviceNetworkStatus,
			retryCount, intf)
		if err != nil {
			log.Fatal(err)
		}
		localTCPAddr := net.TCPAddr{IP: localAddr}
		if debug {
			fmt.Printf("Connecting to %s using intf %s source %v\n",
				configUrl, intf, localTCPAddr)
		}
		d := net.Dialer{LocalAddr: &localTCPAddr}
		transport := &http.Transport{
			TLSClientConfig: tlsConfig,
			Dial:            d.Dial,
		}
		client := &http.Client{Transport: transport}
		req, err := http.NewRequest("GET", "https://"+configUrl, nil)
		if err != nil {
			fmt.Println(err)
			continue
		}
		trace := &httptrace.ClientTrace{
			GotConn: func(connInfo httptrace.GotConnInfo) {
				fmt.Printf("Got RemoteAddr: %+v, LocalAddr: %+v\n",
					connInfo.Conn.RemoteAddr(),
					connInfo.Conn.LocalAddr())
			},
		}
		req = req.WithContext(httptrace.WithClientTrace(req.Context(),
			trace))
		resp, err := client.Do(req)
		if err != nil {
			log.Printf("URL get fail: %v\n", err)
			continue
		}
		defer resp.Body.Close()
		connState := resp.TLS
		if connState == nil {
			log.Println("no TLS connection state")
			// Inform ledmanager about broken cloud connectivity
			types.UpdateLedManagerConfig(10)
			continue
		}

		if connState.OCSPResponse == nil ||
			!stapledCheck(connState) {
			if connState.OCSPResponse == nil {
				log.Printf("no OCSP response for %s\n",
					configUrl)
			} else {
				log.Printf("OCSP stapled check failed for %s\n",
					configUrl)
			}
			//XXX OSCP is not implemented in cloud side so
			// commenting out it for now. Should be:
			// Inform ledmanager about broken cloud connectivity
			// types.UpdateLedManagerConfig(10)
			// continue
		}
		// Even if we get a 404 we consider the connection a success
		zedCloudSuccess(intf)

		// now cloud connectivity is good, mark partition state as
		// active if it was inprogress
		// XXX down the road we want more diagnostics and validation
		// before we do this
		curPart := getCurrentPartition()
		if  isCurrentPartitionStateInProgress() {
			log.Printf("Config Fetch Task, curPart %s inprogress\n",
				curPart)
			if err := markPartitionStateActive(); err != nil {
				log.Println(err)
			}
		}

		if err := validateConfigMessage(configUrl, intf, localTCPAddr,
			resp); err != nil {
			log.Println("validateConfigMessage: ", err)
			// Inform ledmanager about cloud connectivity
			types.UpdateLedManagerConfig(3)
			return
		}

		changed, config, err := readDeviceConfigProtoMessage(resp)
		if err != nil {
			log.Println("readDeviceConfigProtoMessage: ", err)
			// Inform ledmanager about cloud connectivity
			types.UpdateLedManagerConfig(3)
			return
		}

		// Inform ledmanager about config received from cloud
		types.UpdateLedManagerConfig(4)
		if !changed {
			if debug {
				log.Printf("Configuration from zedcloud is unchanged\n")
			}
			return
		}
		inhaleDeviceConfig(config)
		return
	}
	log.Printf("All attempts to connect to %s using intf %s failed\n",
		configUrl, intf)
	zedCloudFailure(intf)
}

func validateConfigMessage(configUrl string, intf string,
	localTCPAddr net.TCPAddr, r *http.Response) error {

	var ctTypeStr = "Content-Type"
	var ctTypeProtoStr = "application/x-proto-binary"

	switch r.StatusCode {
	case http.StatusOK:
		if debug {
			fmt.Printf("validateConfigMessage %s using intf %s source %v StatusOK\n",
				configUrl, intf, localTCPAddr)
		}
	default:
		log.Printf("validateConfigMessage %s using intf %s source %v statuscode %d %s\n",
			configUrl, intf, localTCPAddr,
			r.StatusCode, http.StatusText(r.StatusCode))
		if debug {
			fmt.Printf("received response %v\n", r)
		}
		return fmt.Errorf("http status %d %s",
			r.StatusCode, http.StatusText(r.StatusCode))
	}
	ct := r.Header.Get(ctTypeStr)
	if ct == "" {
		return fmt.Errorf("No content-type")
	}
	mimeType, _, err := mime.ParseMediaType(ct)
	if err != nil {
		return fmt.Errorf("Get Content-type error")
	}
	switch mimeType {
	case ctTypeProtoStr:
		return nil
	default:
		return fmt.Errorf("Content-type %s not supported",
			mimeType)
	}
}

var prevConfigHash []byte

// Returns changed, config, error. The changed is based on a comparison of
// the hash of the protobuf message.
func readDeviceConfigProtoMessage(r *http.Response) (bool, *zconfig.EdgeDevConfig, error) {

	var config = &zconfig.EdgeDevConfig{}

	b, err := ioutil.ReadAll(r.Body)
	if err != nil {
		fmt.Println(err)
		return false, nil, err
	}
	// compute sha256 of the image and match it
	// with the one in config file...
	h := sha256.New()
	h.Write(b)
	configHash := h.Sum(nil)
	same := bytes.Equal(configHash, prevConfigHash)
	prevConfigHash = configHash

	//log.Println(" proto bytes(config) received from cloud: ", fmt.Sprintf("%s",bytes))
	//log.Printf("parsing proto %d bytes\n", len(b))
	err = proto.Unmarshal(b, config)
	if err != nil {
		log.Println("Unmarshalling failed: %v", err)
		return false, nil, err
	}
	return !same, config, nil
}

func inhaleDeviceConfig(config *zconfig.EdgeDevConfig) {
	activeVersion := ""

	log.Printf("Inhaling config %v\n", config)

	// if they match return
	var devId = &zconfig.UUIDandVersion{}

	devId = config.GetId()
	if devId != nil {
		if deviceId == "" {
			// First time; record id and version
			log.Printf("First config; storing UUID/version %s/%s\n",
				devId.Uuid, devId.Version)
			deviceId = devId.Uuid
			activeVersion = devId.Version
			// XXX need to update hostname/LISP with deviceId
			// Write to uuid file etc.
		} else {
			// check the device id and version
			if deviceId != devId.Uuid {
				log.Printf("Updated config but wrong UUID have %s got %s\n",
					deviceId, devId.Uuid)
				// XXX can we send back an error somehow?
				return
			}
			// XXX at some point in time we should set version in
			// zedcloud and increment on change, or skip this completely
			// For now we always accept the empty version.
			if devId.Version != "" &&
				devId.Version == activeVersion {
				log.Printf("Same version, ignoring %s\n",
					devId.Version)
				return
			}
			activeVersion = devId.Version
		}
	}
	handleLookUpParam(config)

	// delete old app configs, if any
	checkCurrentAppFiles(config)

	// delete old base os configs, if any
	checkCurrentBaseOsFiles(config)

	// add new App instances
	parseConfig(config)
}

func checkCurrentAppFiles(config *zconfig.EdgeDevConfig) {

	// get the current set of App files
	curAppFilenames, err := ioutil.ReadDir(zedmanagerConfigDirname)
	if err != nil {
		log.Printf("%v for %s\n", err, zedmanagerConfigDirname)
		curAppFilenames = nil
	}

	Apps := config.GetApps()
	// delete any app instances which are not present in the new set
	for _, curApp := range curAppFilenames {
		curAppFilename := curApp.Name()

		// file type json
		if strings.HasSuffix(curAppFilename, ".json") {
			found := false
			for _, app := range Apps {
				appFilename := app.Uuidandversion.Uuid + ".json"
				if appFilename == curAppFilename {
					found = true
					break
				}
			}
			// app instance not found, delete
			if !found {
				log.Printf("Remove app config %s\n", curAppFilename)
				err := os.Remove(zedmanagerConfigDirname + "/" + curAppFilename)
				if err != nil {
					log.Println("Old config: ", err)
				}
				// also remove the certifiates holder config
				os.Remove(zedagentCertObjConfigDirname + "/" + curAppFilename)
			}
		}
	}
}

func checkCurrentBaseOsFiles(config *zconfig.EdgeDevConfig) {

	// get the current set of baseOs files
	curBaseOsFilenames, err := ioutil.ReadDir(zedagentBaseOsConfigDirname)
	if err != nil {
		log.Printf("%v for %s\n", err, zedagentBaseOsConfigDirname)
		curBaseOsFilenames = nil
	}

	baseOses := config.GetBase()
	// delete any baseOs config which is not present in the new set
	for _, curBaseOs := range curBaseOsFilenames {
		curBaseOsFilename := curBaseOs.Name()

		// file type json
		if strings.HasSuffix(curBaseOsFilename, ".json") {
			found := false
			for _, baseOs := range baseOses {
				baseOsFilename := baseOs.Uuidandversion.Uuid + ".json"
				if baseOsFilename == curBaseOsFilename {
					found = true
					break
				}
			}
			// baseOS instance not found, delete
			if !found {
				log.Printf("Remove baseOs config %s\n", curBaseOsFilename)
				err := os.Remove(zedagentBaseOsConfigDirname + "/" + curBaseOsFilename)
				if err != nil {
					log.Printf("Old config:%v\n", err)
				}
				// remove the certificates holder config
				os.Remove(zedagentCertObjConfigDirname + "/" + curBaseOsFilename)
				// also remove the partition info holder config
				os.Remove(configDir + "/" + curBaseOsFilename)
			}
		}
	}
}

func stapledCheck(connState *tls.ConnectionState) bool {
	issuer := connState.VerifiedChains[0][1]
	resp, err := ocsp.ParseResponse(connState.OCSPResponse, issuer)
	if err != nil {
		log.Println("error parsing response: ", err)
		return false
	}
	now := time.Now()
	age := now.Unix() - resp.ProducedAt.Unix()
	remain := resp.NextUpdate.Unix() - now.Unix()
	if debug {
		log.Printf("OCSP age %d, remain %d\n", age, remain)
	}
	if remain < 0 {
		log.Println("OCSP expired.")
		return false
	}
	if resp.Status == ocsp.Good {
		if debug {
			log.Println("Certificate Status Good.")
		}
	} else if resp.Status == ocsp.Unknown {
		log.Println("Certificate Status Unknown")
	} else {
		log.Println("Certificate Status Revoked")
	}
	return resp.Status == ocsp.Good
}
