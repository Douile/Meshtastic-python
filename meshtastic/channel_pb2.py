# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: channel.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rchannel.proto\"\xf6\x02\n\x0f\x43hannelSettings\x12\x10\n\x08tx_power\x18\x01 \x01(\x05\x12\x32\n\x0cmodem_config\x18\x03 \x01(\x0e\x32\x1c.ChannelSettings.ModemConfig\x12\x11\n\tbandwidth\x18\x06 \x01(\r\x12\x15\n\rspread_factor\x18\x07 \x01(\r\x12\x13\n\x0b\x63oding_rate\x18\x08 \x01(\r\x12\x13\n\x0b\x63hannel_num\x18\t \x01(\r\x12\x0b\n\x03psk\x18\x04 \x01(\x0c\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\n\n\x02id\x18\n \x01(\x07\x12\x16\n\x0euplink_enabled\x18\x10 \x01(\x08\x12\x18\n\x10\x64ownlink_enabled\x18\x11 \x01(\x08\"p\n\x0bModemConfig\x12\r\n\tVLongSlow\x10\x00\x12\x0c\n\x08LongSlow\x10\x01\x12\x0c\n\x08LongFast\x10\x02\x12\x0b\n\x07MidSlow\x10\x03\x12\x0b\n\x07MidFast\x10\x04\x12\r\n\tShortSlow\x10\x05\x12\r\n\tShortFast\x10\x06\"\x8b\x01\n\x07\x43hannel\x12\r\n\x05index\x18\x01 \x01(\x05\x12\"\n\x08settings\x18\x02 \x01(\x0b\x32\x10.ChannelSettings\x12\x1b\n\x04role\x18\x03 \x01(\x0e\x32\r.Channel.Role\"0\n\x04Role\x12\x0c\n\x08\x44ISABLED\x10\x00\x12\x0b\n\x07PRIMARY\x10\x01\x12\r\n\tSECONDARY\x10\x02\x42I\n\x13\x63om.geeksville.meshB\rChannelProtosH\x03Z!github.com/meshtastic/gomeshprotob\x06proto3')



_CHANNELSETTINGS = DESCRIPTOR.message_types_by_name['ChannelSettings']
_CHANNEL = DESCRIPTOR.message_types_by_name['Channel']
_CHANNELSETTINGS_MODEMCONFIG = _CHANNELSETTINGS.enum_types_by_name['ModemConfig']
_CHANNEL_ROLE = _CHANNEL.enum_types_by_name['Role']
ChannelSettings = _reflection.GeneratedProtocolMessageType('ChannelSettings', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELSETTINGS,
  '__module__' : 'channel_pb2'
  # @@protoc_insertion_point(class_scope:ChannelSettings)
  })
_sym_db.RegisterMessage(ChannelSettings)

Channel = _reflection.GeneratedProtocolMessageType('Channel', (_message.Message,), {
  'DESCRIPTOR' : _CHANNEL,
  '__module__' : 'channel_pb2'
  # @@protoc_insertion_point(class_scope:Channel)
  })
_sym_db.RegisterMessage(Channel)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\rChannelProtosH\003Z!github.com/meshtastic/gomeshproto'
  _CHANNELSETTINGS._serialized_start=18
  _CHANNELSETTINGS._serialized_end=392
  _CHANNELSETTINGS_MODEMCONFIG._serialized_start=280
  _CHANNELSETTINGS_MODEMCONFIG._serialized_end=392
  _CHANNEL._serialized_start=395
  _CHANNEL._serialized_end=534
  _CHANNEL_ROLE._serialized_start=486
  _CHANNEL_ROLE._serialized_end=534
# @@protoc_insertion_point(module_scope)
