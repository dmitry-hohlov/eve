FROM alpine:3.12
WORKDIR /
# hadolint ignore=DL3018
RUN apk add --no-cache bash glib squashfs-tools util-linux e2fsprogs \
        e2fsprogs-extra keyutils dosfstools coreutils sgdisk smartmontools=7.1-r2
COPY storage-init.sh /

ENTRYPOINT []
CMD ["/storage-init.sh"]
