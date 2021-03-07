import os
import xml.etree.ElementTree as ET

from configparser import ConfigParser, NoOptionError, NoSectionError, MissingSectionHeaderError, ParsingError
from common import utils


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


    def set_os_varian(self, arch,  dev ):
        """ set os type     """
        os = ET.SubElement(self.domain, 'os')
        type = ET.SubElement(
            os, 'type', {'arch': arch})
        type.text = 'hvm'
        ET.SubElement(os, 'boot', {'dev': dev})                        

        

        

       