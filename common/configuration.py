import os

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
