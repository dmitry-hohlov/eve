# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mesh.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import netcmn_pb2 as netcmn__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mesh.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\n\037com.zededa.cloud.uservice.protoZ$github.com/lf-edge/eve/api/go/config'),
  serialized_pb=_b('\n\nmesh.proto\x1a\x0cnetcmn.proto\"1\n\tMapServer\x12\x10\n\x08NameOrIp\x18\x01 \x01(\t\x12\x12\n\nCredential\x18\x02 \x01(\t\"\xf5\x01\n\x11\x44\x65viceLispDetails\x12\"\n\x0eLispMapServers\x18\x01 \x03(\x0b\x32\n.MapServer\x12\x14\n\x0cLispInstance\x18\x02 \x01(\r\x12\x0b\n\x03\x45ID\x18\x04 \x01(\t\x12\x12\n\nEIDHashLen\x18\x05 \x01(\r\x12\x1e\n\nZedServers\x18\x06 \x03(\x0b\x32\n.ZedServer\x12\x1b\n\x13\x45idAllocationPrefix\x18\x08 \x01(\x0c\x12\x1e\n\x16\x45idAllocationPrefixLen\x18\t \x01(\r\x12\x12\n\nClientAddr\x18\n \x01(\t\x12\x14\n\x0c\x45xperimental\x18\x14 \x01(\x08\x42G\n\x1f\x63om.zededa.cloud.uservice.protoZ$github.com/lf-edge/eve/api/go/configb\x06proto3')
  ,
  dependencies=[netcmn__pb2.DESCRIPTOR,])




_MAPSERVER = _descriptor.Descriptor(
  name='MapServer',
  full_name='MapServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='NameOrIp', full_name='MapServer.NameOrIp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Credential', full_name='MapServer.Credential', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=77,
)


_DEVICELISPDETAILS = _descriptor.Descriptor(
  name='DeviceLispDetails',
  full_name='DeviceLispDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='LispMapServers', full_name='DeviceLispDetails.LispMapServers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='LispInstance', full_name='DeviceLispDetails.LispInstance', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='EID', full_name='DeviceLispDetails.EID', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='EIDHashLen', full_name='DeviceLispDetails.EIDHashLen', index=3,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ZedServers', full_name='DeviceLispDetails.ZedServers', index=4,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='EidAllocationPrefix', full_name='DeviceLispDetails.EidAllocationPrefix', index=5,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='EidAllocationPrefixLen', full_name='DeviceLispDetails.EidAllocationPrefixLen', index=6,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ClientAddr', full_name='DeviceLispDetails.ClientAddr', index=7,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Experimental', full_name='DeviceLispDetails.Experimental', index=8,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=325,
)

_DEVICELISPDETAILS.fields_by_name['LispMapServers'].message_type = _MAPSERVER
_DEVICELISPDETAILS.fields_by_name['ZedServers'].message_type = netcmn__pb2._ZEDSERVER
DESCRIPTOR.message_types_by_name['MapServer'] = _MAPSERVER
DESCRIPTOR.message_types_by_name['DeviceLispDetails'] = _DEVICELISPDETAILS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MapServer = _reflection.GeneratedProtocolMessageType('MapServer', (_message.Message,), dict(
  DESCRIPTOR = _MAPSERVER,
  __module__ = 'mesh_pb2'
  # @@protoc_insertion_point(class_scope:MapServer)
  ))
_sym_db.RegisterMessage(MapServer)

DeviceLispDetails = _reflection.GeneratedProtocolMessageType('DeviceLispDetails', (_message.Message,), dict(
  DESCRIPTOR = _DEVICELISPDETAILS,
  __module__ = 'mesh_pb2'
  # @@protoc_insertion_point(class_scope:DeviceLispDetails)
  ))
_sym_db.RegisterMessage(DeviceLispDetails)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)