# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_bNum', [dirname(__file__)])
        except ImportError:
            import _bNum
            return _bNum
        if fp is not None:
            try:
                _mod = imp.load_module('_bNum', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _bNum = swig_import_helper()
    del swig_import_helper
else:
    import _bNum
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class bNum(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, bNum, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, bNum, name)
    __repr__ = _swig_repr
    __swig_setmethods__["size"] = _bNum.bNum_size_set
    __swig_getmethods__["size"] = _bNum.bNum_size_get
    if _newclass:size = _swig_property(_bNum.bNum_size_get, _bNum.bNum_size_set)
    __swig_setmethods__["sign"] = _bNum.bNum_sign_set
    __swig_getmethods__["sign"] = _bNum.bNum_sign_get
    if _newclass:sign = _swig_property(_bNum.bNum_sign_get, _bNum.bNum_sign_set)
    __swig_setmethods__["base"] = _bNum.bNum_base_set
    __swig_getmethods__["base"] = _bNum.bNum_base_get
    if _newclass:base = _swig_property(_bNum.bNum_base_get, _bNum.bNum_base_set)
    __swig_setmethods__["nums"] = _bNum.bNum_nums_set
    __swig_getmethods__["nums"] = _bNum.bNum_nums_get
    if _newclass:nums = _swig_property(_bNum.bNum_nums_get, _bNum.bNum_nums_set)
    def __init__(self): 
        this = _bNum.new_bNum()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _bNum.delete_bNum
    __del__ = lambda self : None;
bNum_swigregister = _bNum.bNum_swigregister
bNum_swigregister(bNum)


def StructFromStr(*args):
  return _bNum.StructFromStr(*args)
StructFromStr = _bNum.StructFromStr

def frInt(*args):
  return _bNum.frInt(*args)
frInt = _bNum.frInt

def getString(*args):
  return _bNum.getString(*args)
getString = _bNum.getString

def copy(*args):
  return _bNum.copy(*args)
copy = _bNum.copy

def DelZeros(*args):
  return _bNum.DelZeros(*args)
DelZeros = _bNum.DelZeros

def compare(*args):
  return _bNum.compare(*args)
compare = _bNum.compare

def Sum1(*args):
  return _bNum.Sum1(*args)
Sum1 = _bNum.Sum1

def Sum2(*args):
  return _bNum.Sum2(*args)
Sum2 = _bNum.Sum2

def sub(*args):
  return _bNum.sub(*args)
sub = _bNum.sub

def mins(*args):
  return _bNum.mins(*args)
mins = _bNum.mins

def mul(*args):
  return _bNum.mul(*args)
mul = _bNum.mul

def dividing(*args):
  return _bNum.dividing(*args)
dividing = _bNum.dividing

def shiftLeft(*args):
  return _bNum.shiftLeft(*args)
shiftLeft = _bNum.shiftLeft

def pPow(*args):
  return _bNum.pPow(*args)
pPow = _bNum.pPow

def powMod(*args):
  return _bNum.powMod(*args)
powMod = _bNum.powMod

def ReadFromTFile(*args):
  return _bNum.ReadFromTFile(*args)
ReadFromTFile = _bNum.ReadFromTFile

def WriteToTFile(*args):
  return _bNum.WriteToTFile(*args)
WriteToTFile = _bNum.WriteToTFile

def ReadFromBFile(*args):
  return _bNum.ReadFromBFile(*args)
ReadFromBFile = _bNum.ReadFromBFile

def WriteToBFile(*args):
  return _bNum.WriteToBFile(*args)
WriteToBFile = _bNum.WriteToBFile
# This file is compatible with both classic and new-style classes.


