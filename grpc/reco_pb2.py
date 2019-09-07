# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reco.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='reco.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nreco.proto\"_\n\x0fRecoRequestArgs\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\x05\x12\x13\n\x0b\x61rticle_num\x18\x03 \x01(\x05\x12\x12\n\ntime_stamp\x18\x04 \x01(\x03\"5\n\x05Track\x12\r\n\x05\x63lick\x18\x01 \x01(\t\x12\x0c\n\x04read\x18\x02 \x01(\t\x12\x0f\n\x07\x63ollect\x18\x03 \x01(\t\"4\n\x07\x41rticle\x12\x12\n\narticle_id\x18\x01 \x01(\x03\x12\x15\n\x05track\x18\x02 \x01(\x0b\x32\x06.Track\"F\n\x10RecoResponseArgs\x12\x16\n\x0epre_time_stamp\x18\x01 \x01(\x03\x12\x1a\n\x08\x61rticles\x18\x02 \x03(\x0b\x32\x08.Article2B\n\x04Reco\x12:\n\x11\x61rticle_recommand\x12\x10.RecoRequestArgs\x1a\x11.RecoResponseArgs\"\x00\x62\x06proto3')
)




_RECOREQUESTARGS = _descriptor.Descriptor(
  name='RecoRequestArgs',
  full_name='RecoRequestArgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='RecoRequestArgs.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='RecoRequestArgs.channel_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='article_num', full_name='RecoRequestArgs.article_num', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='RecoRequestArgs.time_stamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=14,
  serialized_end=109,
)


_TRACK = _descriptor.Descriptor(
  name='Track',
  full_name='Track',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='click', full_name='Track.click', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='read', full_name='Track.read', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collect', full_name='Track.collect', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=111,
  serialized_end=164,
)


_ARTICLE = _descriptor.Descriptor(
  name='Article',
  full_name='Article',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='article_id', full_name='Article.article_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='track', full_name='Article.track', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=166,
  serialized_end=218,
)


_RECORESPONSEARGS = _descriptor.Descriptor(
  name='RecoResponseArgs',
  full_name='RecoResponseArgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pre_time_stamp', full_name='RecoResponseArgs.pre_time_stamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='articles', full_name='RecoResponseArgs.articles', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=220,
  serialized_end=290,
)

_ARTICLE.fields_by_name['track'].message_type = _TRACK
_RECORESPONSEARGS.fields_by_name['articles'].message_type = _ARTICLE
DESCRIPTOR.message_types_by_name['RecoRequestArgs'] = _RECOREQUESTARGS
DESCRIPTOR.message_types_by_name['Track'] = _TRACK
DESCRIPTOR.message_types_by_name['Article'] = _ARTICLE
DESCRIPTOR.message_types_by_name['RecoResponseArgs'] = _RECORESPONSEARGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RecoRequestArgs = _reflection.GeneratedProtocolMessageType('RecoRequestArgs', (_message.Message,), dict(
  DESCRIPTOR = _RECOREQUESTARGS,
  __module__ = 'reco_pb2'
  # @@protoc_insertion_point(class_scope:RecoRequestArgs)
  ))
_sym_db.RegisterMessage(RecoRequestArgs)

Track = _reflection.GeneratedProtocolMessageType('Track', (_message.Message,), dict(
  DESCRIPTOR = _TRACK,
  __module__ = 'reco_pb2'
  # @@protoc_insertion_point(class_scope:Track)
  ))
_sym_db.RegisterMessage(Track)

Article = _reflection.GeneratedProtocolMessageType('Article', (_message.Message,), dict(
  DESCRIPTOR = _ARTICLE,
  __module__ = 'reco_pb2'
  # @@protoc_insertion_point(class_scope:Article)
  ))
_sym_db.RegisterMessage(Article)

RecoResponseArgs = _reflection.GeneratedProtocolMessageType('RecoResponseArgs', (_message.Message,), dict(
  DESCRIPTOR = _RECORESPONSEARGS,
  __module__ = 'reco_pb2'
  # @@protoc_insertion_point(class_scope:RecoResponseArgs)
  ))
_sym_db.RegisterMessage(RecoResponseArgs)



_RECO = _descriptor.ServiceDescriptor(
  name='Reco',
  full_name='Reco',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=292,
  serialized_end=358,
  methods=[
  _descriptor.MethodDescriptor(
    name='article_recommand',
    full_name='Reco.article_recommand',
    index=0,
    containing_service=None,
    input_type=_RECOREQUESTARGS,
    output_type=_RECORESPONSEARGS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RECO)

DESCRIPTOR.services_by_name['Reco'] = _RECO

# @@protoc_insertion_point(module_scope)
