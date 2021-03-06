# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Responses/UseItemReviveResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Responses/UseItemReviveResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n;POGOProtos/Networking/Responses/UseItemReviveResponse.proto\x12\x1fPOGOProtos.Networking.Responses\"\xe1\x01\n\x15UseItemReviveResponse\x12M\n\x06result\x18\x01 \x01(\x0e\x32=.POGOProtos.Networking.Responses.UseItemReviveResponse.Result\x12\x0f\n\x07stamina\x18\x02 \x01(\x05\"h\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x14\n\x10\x45RROR_NO_POKEMON\x10\x02\x12\x14\n\x10\x45RROR_CANNOT_USE\x10\x03\x12\x1a\n\x16\x45RROR_DEPLOYED_TO_FORT\x10\x04\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_USEITEMREVIVERESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='POGOProtos.Networking.Responses.UseItemReviveResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NO_POKEMON', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_CANNOT_USE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_DEPLOYED_TO_FORT', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=218,
  serialized_end=322,
)
_sym_db.RegisterEnumDescriptor(_USEITEMREVIVERESPONSE_RESULT)


_USEITEMREVIVERESPONSE = _descriptor.Descriptor(
  name='UseItemReviveResponse',
  full_name='POGOProtos.Networking.Responses.UseItemReviveResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='POGOProtos.Networking.Responses.UseItemReviveResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stamina', full_name='POGOProtos.Networking.Responses.UseItemReviveResponse.stamina', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USEITEMREVIVERESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=322,
)

_USEITEMREVIVERESPONSE.fields_by_name['result'].enum_type = _USEITEMREVIVERESPONSE_RESULT
_USEITEMREVIVERESPONSE_RESULT.containing_type = _USEITEMREVIVERESPONSE
DESCRIPTOR.message_types_by_name['UseItemReviveResponse'] = _USEITEMREVIVERESPONSE

UseItemReviveResponse = _reflection.GeneratedProtocolMessageType('UseItemReviveResponse', (_message.Message,), dict(
  DESCRIPTOR = _USEITEMREVIVERESPONSE,
  __module__ = 'POGOProtos.Networking.Responses.UseItemReviveResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.UseItemReviveResponse)
  ))
_sym_db.RegisterMessage(UseItemReviveResponse)


# @@protoc_insertion_point(module_scope)
