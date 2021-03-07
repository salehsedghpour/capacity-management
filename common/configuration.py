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

<<<<<<< HEAD
               

    def set_vm_disk(self, type, file):
        """
        
            file: absolute path of disk image file
            type: image file formats
          """
        if file is  '':
                return False  
        disk = ET.SubElement('device', 'disk', {'type': 'file', 'device': 'disk'})
        if type is  '':
             type = 'raw'
        
        ET.SubElement(disk, 'source', {'file': file})  

        ET.SubElement(disk, 'driver', {'name': 'qemu', 'type': type})
        ET.SubElement(
            disk, 'target', {'dev': 'vdc' , 'bus': 'virtio'})


    def set_graphics(self, type, port, autoport):
        # graphic device
        ET.SubElement('device', 'graphics', {
                      'type': type, 'port': port, 'autoport': autoport}) 


    def set_os_variant(self, arch,  dev ):
        """ set os type     """
        os = ET.SubElement(self.domain, 'os')
        type = ET.SubElement(
            os, 'type', {'arch': arch})
        type.text = 'hvm'
        ET.SubElement(os, 'boot', {'dev': dev})                        

        

        

       
=======

class LibvirtXMLGenerator():
    """Libvirt XML Generator"""

    def __init__(self):
        """Initialize"""
        super(LibvirtXMLGenerator, self).__init__()

        self.domain = ET.Element('domain')
        self.domain_name = ET.SubElement(self.domain, "name")
        self.domain_memory = ET.SubElement(self.domain, "name")
        self.domain_vcpu = ET.SubElement(self.domain, "vcpu")

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

    def set_domain_name(self, domain_name):
        """Set domain Name
        :rtype: object
        :param domain_name:
        """
        if domain_name != "":
            self.domain_name.text = domain_name
        else:
            raise exceptions.EmptyString

    def set_domain_memory(self, domain_memory, domain_memory_unit):
        """Set domain Memory and its unit
        :rtype: object
        :param domain_memory:
        :param domain_memory_unit:
        """
        if domain_memory_unit in ["b", "bytes", "KB", "K", "KiB", "MB", "M","MiB", "GB", "G","GiB"]:
            self.domain_memory.set("unit", domain_memory_unit)
            self.domain_memory.text = str(domain_memory)
        else:
            raise exceptions.InvalidMemoryUnit

    def set_domain_vcpu(self, vcpu_number):
        """Set the number of VCPUs of domain
        :rtype: object
        :param vcpu_number: 
        """
        try:
            self.domain_vcpu.text = str(int(vcpu_number))
        except ValueError:
            raise ValueError("Value error on VCPU Number")

    #TODO Validation on CPU Set
    def set_domain_vcpu_placement(self, vcpu_placement, cpuset=None):
        """Set the placement of VCPUs
        :rtype: object
        :param vcpu_placement:
        :param cpuset:
        """
        if vcpu_placement == "static":
            self.domain_vcpu.set("placement", vcpu_placement)
            self.domain_vcpu.set("cpuset", cpuset)
        elif vcpu_placement == "auto":
            self.domain_vcpu.set("placement", vcpu_placement)
        else:
            raise exceptions.InvalidVCPUPlacement


>>>>>>> main
