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

    def make_config(self, name, disk_path, ram, vcpu, image):      
        """ create a domain"""
        domxml = """<domain type='kvm'>
          <name>"""+name+"""</name>
          <memory>"""+ram+"""</memory>
          <vcpu>"""+vcpu+"""</vcpu>
          <os>
            <type arch='x86_64' machine='pc-0.13'>hvm</type>
          </os>
          <devices>
            <disk type='file' device='disk'>
              <driver name='qemu' type='qed'/>
              <source file="""+image+""" />
              <target dev='vda' bus='virtio'/>
            </disk>
          </devices>
         </domain>""" 
        
        dom = self.connection.defineXML(domxml)
        return dom 

    def read_config(self,path_to_xml_config):
        """Read Config File"""
        with open(path_to_xml_config, "r") as f:           
            xml = f.readlines()
        return xml
    