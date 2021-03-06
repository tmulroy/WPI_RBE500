# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from pa1/HTRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class HTRequest(genpy.Message):
  _md5sum = "b73c7247aab620f8f17139f7c17d037f"
  _type = "pa1/HTRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float64 ht11
float64 ht12
float64 ht13
float64 ht14
float64 ht21
float64 ht22
float64 ht23
float64 ht24
float64 ht31
float64 ht32
float64 ht33
float64 ht34
float64 ht41
float64 ht42
float64 ht43
float64 ht44
"""
  __slots__ = ['ht11','ht12','ht13','ht14','ht21','ht22','ht23','ht24','ht31','ht32','ht33','ht34','ht41','ht42','ht43','ht44']
  _slot_types = ['float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ht11,ht12,ht13,ht14,ht21,ht22,ht23,ht24,ht31,ht32,ht33,ht34,ht41,ht42,ht43,ht44

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(HTRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.ht11 is None:
        self.ht11 = 0.
      if self.ht12 is None:
        self.ht12 = 0.
      if self.ht13 is None:
        self.ht13 = 0.
      if self.ht14 is None:
        self.ht14 = 0.
      if self.ht21 is None:
        self.ht21 = 0.
      if self.ht22 is None:
        self.ht22 = 0.
      if self.ht23 is None:
        self.ht23 = 0.
      if self.ht24 is None:
        self.ht24 = 0.
      if self.ht31 is None:
        self.ht31 = 0.
      if self.ht32 is None:
        self.ht32 = 0.
      if self.ht33 is None:
        self.ht33 = 0.
      if self.ht34 is None:
        self.ht34 = 0.
      if self.ht41 is None:
        self.ht41 = 0.
      if self.ht42 is None:
        self.ht42 = 0.
      if self.ht43 is None:
        self.ht43 = 0.
      if self.ht44 is None:
        self.ht44 = 0.
    else:
      self.ht11 = 0.
      self.ht12 = 0.
      self.ht13 = 0.
      self.ht14 = 0.
      self.ht21 = 0.
      self.ht22 = 0.
      self.ht23 = 0.
      self.ht24 = 0.
      self.ht31 = 0.
      self.ht32 = 0.
      self.ht33 = 0.
      self.ht34 = 0.
      self.ht41 = 0.
      self.ht42 = 0.
      self.ht43 = 0.
      self.ht44 = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_16d().pack(_x.ht11, _x.ht12, _x.ht13, _x.ht14, _x.ht21, _x.ht22, _x.ht23, _x.ht24, _x.ht31, _x.ht32, _x.ht33, _x.ht34, _x.ht41, _x.ht42, _x.ht43, _x.ht44))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 128
      (_x.ht11, _x.ht12, _x.ht13, _x.ht14, _x.ht21, _x.ht22, _x.ht23, _x.ht24, _x.ht31, _x.ht32, _x.ht33, _x.ht34, _x.ht41, _x.ht42, _x.ht43, _x.ht44,) = _get_struct_16d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_16d().pack(_x.ht11, _x.ht12, _x.ht13, _x.ht14, _x.ht21, _x.ht22, _x.ht23, _x.ht24, _x.ht31, _x.ht32, _x.ht33, _x.ht34, _x.ht41, _x.ht42, _x.ht43, _x.ht44))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 128
      (_x.ht11, _x.ht12, _x.ht13, _x.ht14, _x.ht21, _x.ht22, _x.ht23, _x.ht24, _x.ht31, _x.ht32, _x.ht33, _x.ht34, _x.ht41, _x.ht42, _x.ht43, _x.ht44,) = _get_struct_16d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_16d = None
def _get_struct_16d():
    global _struct_16d
    if _struct_16d is None:
        _struct_16d = struct.Struct("<16d")
    return _struct_16d
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from pa1/HTResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class HTResponse(genpy.Message):
  _md5sum = "f439218c3a6a6da84daea3b1bccc8aa6"
  _type = "pa1/HTResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float64 q1
float64 q2
float64 d3


"""
  __slots__ = ['q1','q2','d3']
  _slot_types = ['float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       q1,q2,d3

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(HTResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.q1 is None:
        self.q1 = 0.
      if self.q2 is None:
        self.q2 = 0.
      if self.d3 is None:
        self.d3 = 0.
    else:
      self.q1 = 0.
      self.q2 = 0.
      self.d3 = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3d().pack(_x.q1, _x.q2, _x.d3))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.q1, _x.q2, _x.d3,) = _get_struct_3d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3d().pack(_x.q1, _x.q2, _x.d3))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.q1, _x.q2, _x.d3,) = _get_struct_3d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
class HT(object):
  _type          = 'pa1/HT'
  _md5sum = '41bf0543de79fcb6f767b6c9848b88ec'
  _request_class  = HTRequest
  _response_class = HTResponse
