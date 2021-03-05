# coding: utf-8


from __future__ import print_function
import sys
import os
import libvirt

class ConfigEditor(ConfigParser):
    """KVM Configuration Editor"""

    def connect(self, address):
        """ Connect to a domain """
        conn = libvirt.open(address)
        if conn == None:
            print('Failed to open connection to system', file=sys.stderr)
            exit(1)
        else:
            print('Succeeded to open connection to system')
        self.connection = conn
        return self.connection
        #conn.close()
        
        
    