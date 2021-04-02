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
            self.set("GENERAL", "libvirt_images_directory", "/var/lib/libvirt/images/")
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
        self.domain_name = ET.SubElement(self.domain, "name")
        self.domain_memory = ET.SubElement(self.domain, "name")
        self.domain_vcpu = ET.SubElement(self.domain, "vcpu")
        self.domain_devices = ET.SubElement(self.domain, "devices")
        self.domain_devices_disk = ET.SubElement(self.domain_devices, "disk")
        self.domain_devices_graphics =  ET.SubElement(self.domain_devices, 'graphics')
        self.domain_os = ET.SubElement(self.domain, 'os')
        self.domain_os_boot = ET.SubElement(self.domain_os, 'boot')
        self.domain_os_type = ET.SubElement(self.domain_os, 'type')
        

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

    def set_domain_devices_disk_type_device(self, disk_type, disk_device):
        """ Set the disk type and disk device of a device in a domain"""
        disk_types = ["file", "block", "dir", "network", "volume", "nvme", "vhostuser"]
        disk_devices = ["floppy", "disk", "cdrom", "lun"]
        if disk_type in disk_types:
            if disk_device in disk_devices:
                self.domain_devices_disk.set("type", disk_type)
                self.domain_devices_disk.set("device", disk_device)
            else:
                raise exceptions.InvalidDiskDevice
        else:
            raise exceptions.InvalidDiskType       


    def set_graphics(self, graphics_type, port, autoport):
        """Set Graphic Device"""
        graphics_types = ['sdl',' vnc', 'spice', 'rdp', ' desktop',' egl-headless']
        assert(graphics_type != "")
        if graphics_type in graphics_types:
            if autoport in ['yes', 'no']:
                self.domain_devices_graphics.set("graphics_type", graphics_type)
                self.domain_devices_graphics.set("port", port)
                self.domain_devices_graphics.set("autoport", autoport)                
            else:
                raise exceptions.InvalidAutoPort
        else:   
            raise exceptions.InvalidGraphicsType  
    


    def set_os_variant(self, arch, dev):
        """ set os type    """

        assert(arch != "")
        if arch != "":
         
            self.domain_os_type.set('arch',arch)
        else: 
            raise exceptions.EmptyString   
        
        self.domain_os_type.text = 'hvm'

        assert(dev != "")
        if dev in ["fd", "hd", "cdrom", "network"]:
           self.domain_os_boot.set('dev', dev)
        else:
            raise exceptions.InvalidBootDevType
                              

        

 
            


