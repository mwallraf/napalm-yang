
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
  unicode = str
elif six.PY2:
  import __builtin__

from . import config
from . import state
from . import clock
from . import dns
from . import ntp
from . import ssh_server
from . import telnet_server
from . import logging
from . import aaa
from . import memory
from . import processes
class system(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for system-related configuration and
operational state data
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__config','__state','__clock','__dns','__ntp','__ssh_server','__telnet_server','__logging','__aaa','__memory','__processes',)

  _yang_name = 'system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__processes = YANGDynClass(base=processes.processes, is_container='container', yang_name="processes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    self.__logging = YANGDynClass(base=logging.logging, is_container='container', yang_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    self.__clock = YANGDynClass(base=clock.clock, is_container='container', yang_name="clock", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    self.__ntp = YANGDynClass(base=ntp.ntp, is_container='container', yang_name="ntp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    self.__telnet_server = YANGDynClass(base=telnet_server.telnet_server, is_container='container', yang_name="telnet-server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    self.__dns = YANGDynClass(base=dns.dns, is_container='container', yang_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    self.__memory = YANGDynClass(base=memory.memory, is_container='container', yang_name="memory", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    self.__aaa = YANGDynClass(base=aaa.aaa, is_container='container', yang_name="aaa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    self.__ssh_server = YANGDynClass(base=ssh_server.ssh_server, is_container='container', yang_name="ssh-server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

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
      return [u'system']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /system/config (container)

    YANG Description: Global configuration data for the system
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /system/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Global configuration data for the system
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /system/state (container)

    YANG Description: Global operational state data for the system
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /system/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Global operational state data for the system
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _get_clock(self):
    """
    Getter method for clock, mapped from YANG variable /system/clock (container)

    YANG Description: Top-level container for clock configuration data
    """
    return self.__clock
      
  def _set_clock(self, v, load=False):
    """
    Setter method for clock, mapped from YANG variable /system/clock (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_clock is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_clock() directly.

    YANG Description: Top-level container for clock configuration data
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=clock.clock, is_container='container', yang_name="clock", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """clock must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=clock.clock, is_container='container', yang_name="clock", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__clock = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_clock(self):
    self.__clock = YANGDynClass(base=clock.clock, is_container='container', yang_name="clock", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _get_dns(self):
    """
    Getter method for dns, mapped from YANG variable /system/dns (container)

    YANG Description: Enclosing container for DNS resolver data
    """
    return self.__dns
      
  def _set_dns(self, v, load=False):
    """
    Setter method for dns, mapped from YANG variable /system/dns (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dns is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dns() directly.

    YANG Description: Enclosing container for DNS resolver data
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=dns.dns, is_container='container', yang_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dns must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=dns.dns, is_container='container', yang_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__dns = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dns(self):
    self.__dns = YANGDynClass(base=dns.dns, is_container='container', yang_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _get_ntp(self):
    """
    Getter method for ntp, mapped from YANG variable /system/ntp (container)

    YANG Description: Top-level container for NTP configuration and state
    """
    return self.__ntp
      
  def _set_ntp(self, v, load=False):
    """
    Setter method for ntp, mapped from YANG variable /system/ntp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ntp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ntp() directly.

    YANG Description: Top-level container for NTP configuration and state
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ntp.ntp, is_container='container', yang_name="ntp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ntp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ntp.ntp, is_container='container', yang_name="ntp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__ntp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ntp(self):
    self.__ntp = YANGDynClass(base=ntp.ntp, is_container='container', yang_name="ntp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _get_ssh_server(self):
    """
    Getter method for ssh_server, mapped from YANG variable /system/ssh_server (container)

    YANG Description: Top-level container for ssh server
    """
    return self.__ssh_server
      
  def _set_ssh_server(self, v, load=False):
    """
    Setter method for ssh_server, mapped from YANG variable /system/ssh_server (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ssh_server is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ssh_server() directly.

    YANG Description: Top-level container for ssh server
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ssh_server.ssh_server, is_container='container', yang_name="ssh-server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ssh_server must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ssh_server.ssh_server, is_container='container', yang_name="ssh-server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__ssh_server = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ssh_server(self):
    self.__ssh_server = YANGDynClass(base=ssh_server.ssh_server, is_container='container', yang_name="ssh-server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _get_telnet_server(self):
    """
    Getter method for telnet_server, mapped from YANG variable /system/telnet_server (container)

    YANG Description: Top-level container for telnet terminal servers
    """
    return self.__telnet_server
      
  def _set_telnet_server(self, v, load=False):
    """
    Setter method for telnet_server, mapped from YANG variable /system/telnet_server (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_telnet_server is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_telnet_server() directly.

    YANG Description: Top-level container for telnet terminal servers
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=telnet_server.telnet_server, is_container='container', yang_name="telnet-server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """telnet_server must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=telnet_server.telnet_server, is_container='container', yang_name="telnet-server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__telnet_server = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_telnet_server(self):
    self.__telnet_server = YANGDynClass(base=telnet_server.telnet_server, is_container='container', yang_name="telnet-server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _get_logging(self):
    """
    Getter method for logging, mapped from YANG variable /system/logging (container)

    YANG Description: Top-level container for data related to logging / syslog
    """
    return self.__logging
      
  def _set_logging(self, v, load=False):
    """
    Setter method for logging, mapped from YANG variable /system/logging (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_logging is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_logging() directly.

    YANG Description: Top-level container for data related to logging / syslog
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=logging.logging, is_container='container', yang_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """logging must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=logging.logging, is_container='container', yang_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__logging = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_logging(self):
    self.__logging = YANGDynClass(base=logging.logging, is_container='container', yang_name="logging", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _get_aaa(self):
    """
    Getter method for aaa, mapped from YANG variable /system/aaa (container)

    YANG Description: Top-level container for AAA services
    """
    return self.__aaa
      
  def _set_aaa(self, v, load=False):
    """
    Setter method for aaa, mapped from YANG variable /system/aaa (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_aaa is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_aaa() directly.

    YANG Description: Top-level container for AAA services
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=aaa.aaa, is_container='container', yang_name="aaa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """aaa must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=aaa.aaa, is_container='container', yang_name="aaa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__aaa = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_aaa(self):
    self.__aaa = YANGDynClass(base=aaa.aaa, is_container='container', yang_name="aaa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _get_memory(self):
    """
    Getter method for memory, mapped from YANG variable /system/memory (container)

    YANG Description: Top-level container for system memory data
    """
    return self.__memory
      
  def _set_memory(self, v, load=False):
    """
    Setter method for memory, mapped from YANG variable /system/memory (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_memory is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_memory() directly.

    YANG Description: Top-level container for system memory data
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=memory.memory, is_container='container', yang_name="memory", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """memory must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=memory.memory, is_container='container', yang_name="memory", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__memory = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_memory(self):
    self.__memory = YANGDynClass(base=memory.memory, is_container='container', yang_name="memory", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _get_processes(self):
    """
    Getter method for processes, mapped from YANG variable /system/processes (container)

    YANG Description: Parameters related to all monitored processes
    """
    return self.__processes
      
  def _set_processes(self, v, load=False):
    """
    Setter method for processes, mapped from YANG variable /system/processes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_processes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_processes() directly.

    YANG Description: Parameters related to all monitored processes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=processes.processes, is_container='container', yang_name="processes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """processes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=processes.processes, is_container='container', yang_name="processes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__processes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_processes(self):
    self.__processes = YANGDynClass(base=processes.processes, is_container='container', yang_name="processes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  clock = __builtin__.property(_get_clock, _set_clock)
  dns = __builtin__.property(_get_dns, _set_dns)
  ntp = __builtin__.property(_get_ntp, _set_ntp)
  ssh_server = __builtin__.property(_get_ssh_server, _set_ssh_server)
  telnet_server = __builtin__.property(_get_telnet_server, _set_telnet_server)
  logging = __builtin__.property(_get_logging, _set_logging)
  aaa = __builtin__.property(_get_aaa, _set_aaa)
  memory = __builtin__.property(_get_memory, _set_memory)
  processes = __builtin__.property(_get_processes, _set_processes)


  _pyangbind_elements = {'config': config, 'state': state, 'clock': clock, 'dns': dns, 'ntp': ntp, 'ssh_server': ssh_server, 'telnet_server': telnet_server, 'logging': logging, 'aaa': aaa, 'memory': memory, 'processes': processes, }

