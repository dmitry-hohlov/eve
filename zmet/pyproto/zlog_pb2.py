# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zlog.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='zlog.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\nzlog.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd8\x01\n\x08LogEntry\x12\x10\n\x08severity\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x0b\n\x03iid\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12\r\n\x05msgid\x18\x05 \x01(\x04\x12!\n\x04tags\x18\x06 \x03(\x0b\x32\x13.LogEntry.TagsEntry\x12-\n\ttimestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"p\n\tLogBundle\x12\r\n\x05\x64\x65vID\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\t\x12\x16\n\x03log\x18\x03 \x03(\x0b\x32\t.LogEntry\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB=\n\x1f\x63om.zededa.cloud.uservice.protoZ\x1agithub.com/zededa/api/zmetb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_LOGENTRY_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='LogEntry.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='LogEntry.TagsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='LogEntry.TagsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=221,
  serialized_end=264,
)

_LOGENTRY = _descriptor.Descriptor(
  name='LogEntry',
  full_name='LogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='severity', full_name='LogEntry.severity', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='LogEntry.source', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iid', full_name='LogEntry.iid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='LogEntry.content', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msgid', full_name='LogEntry.msgid', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='LogEntry.tags', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='LogEntry.timestamp', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LOGENTRY_TAGSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=264,
)


_LOGBUNDLE = _descriptor.Descriptor(
  name='LogBundle',
  full_name='LogBundle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='devID', full_name='LogBundle.devID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='LogBundle.image', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log', full_name='LogBundle.log', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='LogBundle.timestamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=378,
)

_LOGENTRY_TAGSENTRY.containing_type = _LOGENTRY
_LOGENTRY.fields_by_name['tags'].message_type = _LOGENTRY_TAGSENTRY
_LOGENTRY.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LOGBUNDLE.fields_by_name['log'].message_type = _LOGENTRY
_LOGBUNDLE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['LogEntry'] = _LOGENTRY
DESCRIPTOR.message_types_by_name['LogBundle'] = _LOGBUNDLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogEntry = _reflection.GeneratedProtocolMessageType('LogEntry', (_message.Message,), dict(

  TagsEntry = _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), dict(
    DESCRIPTOR = _LOGENTRY_TAGSENTRY,
    __module__ = 'zlog_pb2'
    # @@protoc_insertion_point(class_scope:LogEntry.TagsEntry)
    ))
  ,
  DESCRIPTOR = _LOGENTRY,
  __module__ = 'zlog_pb2'
  # @@protoc_insertion_point(class_scope:LogEntry)
  ))
_sym_db.RegisterMessage(LogEntry)
_sym_db.RegisterMessage(LogEntry.TagsEntry)

LogBundle = _reflection.GeneratedProtocolMessageType('LogBundle', (_message.Message,), dict(
  DESCRIPTOR = _LOGBUNDLE,
  __module__ = 'zlog_pb2'
  # @@protoc_insertion_point(class_scope:LogBundle)
  ))
_sym_db.RegisterMessage(LogBundle)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\037com.zededa.cloud.uservice.protoZ\032github.com/zededa/api/zmet'))
_LOGENTRY_TAGSENTRY.has_options = True
_LOGENTRY_TAGSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
