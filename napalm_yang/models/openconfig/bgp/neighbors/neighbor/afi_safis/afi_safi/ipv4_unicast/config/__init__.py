
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp - based on the path /bgp/neighbors/neighbor/afi-safis/afi-safi/ipv4-unicast/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for common IPv4 and IPv6 unicast
AFI-SAFI options
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__send_default_route',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'bgp', u'neighbors', u'neighbor', u'afi-safis', u'afi-safi', u'ipv4-unicast', u'config']

  def _get_send_default_route(self):
    """
    Getter method for send_default_route, mapped from YANG variable /bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)

    YANG Description: If set to true, send the default-route to the neighbour(s)
    """
    return self.__send_default_route
      
  def _set_send_default_route(self, v, load=False):
    """
    Setter method for send_default_route, mapped from YANG variable /bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_send_default_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_send_default_route() directly.

    YANG Description: If set to true, send the default-route to the neighbour(s)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """send_default_route must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)""",
        })

    self.__send_default_route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_send_default_route(self):
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)

  send_default_route = __builtin__.property(_get_send_default_route, _set_send_default_route)


  _pyangbind_elements = {'send_default_route': send_default_route, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-common - based on the path /bgp/neighbors/neighbor/afi-safis/afi-safi/ipv4-unicast/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for common IPv4 and IPv6 unicast
AFI-SAFI options
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__send_default_route',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'bgp', u'neighbors', u'neighbor', u'afi-safis', u'afi-safi', u'ipv4-unicast', u'config']

  def _get_send_default_route(self):
    """
    Getter method for send_default_route, mapped from YANG variable /bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)

    YANG Description: If set to true, send the default-route to the neighbour(s)
    """
    return self.__send_default_route
      
  def _set_send_default_route(self, v, load=False):
    """
    Setter method for send_default_route, mapped from YANG variable /bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_send_default_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_send_default_route() directly.

    YANG Description: If set to true, send the default-route to the neighbour(s)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """send_default_route must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)""",
        })

    self.__send_default_route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_send_default_route(self):
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)

  send_default_route = __builtin__.property(_get_send_default_route, _set_send_default_route)


  _pyangbind_elements = {'send_default_route': send_default_route, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-common-multiprotocol - based on the path /bgp/neighbors/neighbor/afi-safis/afi-safi/ipv4-unicast/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for common IPv4 and IPv6 unicast
AFI-SAFI options
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__send_default_route',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'bgp', u'neighbors', u'neighbor', u'afi-safis', u'afi-safi', u'ipv4-unicast', u'config']

  def _get_send_default_route(self):
    """
    Getter method for send_default_route, mapped from YANG variable /bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)

    YANG Description: If set to true, send the default-route to the neighbour(s)
    """
    return self.__send_default_route
      
  def _set_send_default_route(self, v, load=False):
    """
    Setter method for send_default_route, mapped from YANG variable /bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_send_default_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_send_default_route() directly.

    YANG Description: If set to true, send the default-route to the neighbour(s)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """send_default_route must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)""",
        })

    self.__send_default_route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_send_default_route(self):
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)

  send_default_route = __builtin__.property(_get_send_default_route, _set_send_default_route)


  _pyangbind_elements = {'send_default_route': send_default_route, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-common-structure - based on the path /bgp/neighbors/neighbor/afi-safis/afi-safi/ipv4-unicast/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for common IPv4 and IPv6 unicast
AFI-SAFI options
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__send_default_route',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'bgp', u'neighbors', u'neighbor', u'afi-safis', u'afi-safi', u'ipv4-unicast', u'config']

  def _get_send_default_route(self):
    """
    Getter method for send_default_route, mapped from YANG variable /bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)

    YANG Description: If set to true, send the default-route to the neighbour(s)
    """
    return self.__send_default_route
      
  def _set_send_default_route(self, v, load=False):
    """
    Setter method for send_default_route, mapped from YANG variable /bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_send_default_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_send_default_route() directly.

    YANG Description: If set to true, send the default-route to the neighbour(s)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """send_default_route must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)""",
        })

    self.__send_default_route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_send_default_route(self):
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)

  send_default_route = __builtin__.property(_get_send_default_route, _set_send_default_route)


  _pyangbind_elements = {'send_default_route': send_default_route, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-peer-group - based on the path /bgp/neighbors/neighbor/afi-safis/afi-safi/ipv4-unicast/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for common IPv4 and IPv6 unicast
AFI-SAFI options
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__send_default_route',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'bgp', u'neighbors', u'neighbor', u'afi-safis', u'afi-safi', u'ipv4-unicast', u'config']

  def _get_send_default_route(self):
    """
    Getter method for send_default_route, mapped from YANG variable /bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)

    YANG Description: If set to true, send the default-route to the neighbour(s)
    """
    return self.__send_default_route
      
  def _set_send_default_route(self, v, load=False):
    """
    Setter method for send_default_route, mapped from YANG variable /bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_send_default_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_send_default_route() directly.

    YANG Description: If set to true, send the default-route to the neighbour(s)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """send_default_route must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)""",
        })

    self.__send_default_route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_send_default_route(self):
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)

  send_default_route = __builtin__.property(_get_send_default_route, _set_send_default_route)


  _pyangbind_elements = {'send_default_route': send_default_route, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-neighbor - based on the path /bgp/neighbors/neighbor/afi-safis/afi-safi/ipv4-unicast/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for common IPv4 and IPv6 unicast
AFI-SAFI options
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__send_default_route',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'bgp', u'neighbors', u'neighbor', u'afi-safis', u'afi-safi', u'ipv4-unicast', u'config']

  def _get_send_default_route(self):
    """
    Getter method for send_default_route, mapped from YANG variable /bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)

    YANG Description: If set to true, send the default-route to the neighbour(s)
    """
    return self.__send_default_route
      
  def _set_send_default_route(self, v, load=False):
    """
    Setter method for send_default_route, mapped from YANG variable /bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_send_default_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_send_default_route() directly.

    YANG Description: If set to true, send the default-route to the neighbour(s)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """send_default_route must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)""",
        })

    self.__send_default_route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_send_default_route(self):
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)

  send_default_route = __builtin__.property(_get_send_default_route, _set_send_default_route)


  _pyangbind_elements = {'send_default_route': send_default_route, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp-global - based on the path /bgp/neighbors/neighbor/afi-safis/afi-safi/ipv4-unicast/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for common IPv4 and IPv6 unicast
AFI-SAFI options
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__send_default_route',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'bgp', u'neighbors', u'neighbor', u'afi-safis', u'afi-safi', u'ipv4-unicast', u'config']

  def _get_send_default_route(self):
    """
    Getter method for send_default_route, mapped from YANG variable /bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)

    YANG Description: If set to true, send the default-route to the neighbour(s)
    """
    return self.__send_default_route
      
  def _set_send_default_route(self, v, load=False):
    """
    Setter method for send_default_route, mapped from YANG variable /bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/config/send_default_route (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_send_default_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_send_default_route() directly.

    YANG Description: If set to true, send the default-route to the neighbour(s)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """send_default_route must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)""",
        })

    self.__send_default_route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_send_default_route(self):
    self.__send_default_route = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="send-default-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=True)

  send_default_route = __builtin__.property(_get_send_default_route, _set_send_default_route)


  _pyangbind_elements = {'send_default_route': send_default_route, }


