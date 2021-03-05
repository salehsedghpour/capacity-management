import os
import xml.etree.ElementTree as ET

from configparser import ConfigParser, NoOptionError, NoSectionError, MissingSectionHeaderError, ParsingError
from common import utils, exceptions


class ConfigManager(ConfigParser):
    """Configuration Manager"""

    def __init__(self):
        """Initialize """
        super(ConfigManager, self).__init__()

        app_dir = utils.app_dir()
        self._configfile = "{}/config.ini".format(app_dir)
        self._init_config_file()
        self._read_config()

    def _init_config_file(self):
        """Initialize Base Config file"""
        if not os.path.exists(self._configfile):
            self.add_section("GENERAL"),
            self.set("GENERAL", "libvirt_directory", "/etc/libvirt/qemu/")
            self.add_section("CLUSTER_SETUP")
            self.set("CLUSTER_SETUP", "number_of_nodes", "3")
            self.save()

    def _read_config(self):
        """Read Configuration file"""
        if os.path.exists(self._configfile):
            try:
                ConfigManager.read(self, self._configfile)
            except MissingSectionHeaderError:
                return "Error Missing Section header in config file: {}".format(self._configfile)
            except ParsingError:
                return "Error in parsing config file: {}".format(self._configfile)

    def save(self):
        """Write configuration file"""
        with open(self._configfile, 'w') as fd:
            try:
                self.write(fd)
                fd.close()
            except IOError:
                return "Unable to write file on disk."


class LibvirtXMLGenerator():
    """Libvirt XML Generator"""

    def __init__(self):
        """Initialize"""
        super(LibvirtXMLGenerator, self).__init__()

        self.domain = ET.Element('domain')

    def _read_VM_config(self, name):
        libvirt_dir = utils.libvirt_dir()
        self.libvirt_path = "{}/{}.xml".format(libvirt_dir, name)
        if os.path.exists(self._libvirt_path):
            self.vm_xml = ET.parse(self._libvirt_path)
        else:
            self.vm_xml = None

    def set_domain_type(self, domain_type):
        """Set domain type"""
        if domain_type in ["kvm"]:
            self.domain.set("type", domain_type)
        else:
            raise exceptions.InvalidDomainType

    def set_domain_ID(self, domain_id):
        """Set domain ID
        :rtype: object
        :param domain_id: 
        """
        try:
            int_domain_id = int(domain_id)
            self.domain.set("id", str(int_domain_id))
        except ValueError:
            raise exceptions.InvalidDomainID
