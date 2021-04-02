import pytest

from common.configuration import LibvirtXMLGenerator
from common import exceptions


LibvirtXML = LibvirtXMLGenerator()


class TestLibvirtXMLGenerator(object):
    def test_set_domain_type_kvm(self):
        LibvirtXML.set_domain_type_kvm()
        assert "kvm" == LibvirtXML.domain.get("type")

    def test_set_domain_ID(self):
        LibvirtXML.set_domain_ID("2")
        assert "2" == LibvirtXML.domain.get("id")

    def test_set_domain_id_error(self):
        with pytest.raises(exceptions.InvalidDomainID):
            LibvirtXML.set_domain_ID("test")

    def test_set_domain_name(self):
        LibvirtXML.set_domain_name("test")
        assert "test" == LibvirtXML.domain_name.text

    def test_set_empty_domain_name(self):
        with pytest.raises(exceptions.EmptyString):
            LibvirtXML.set_domain_name("")

    def test_set_domain_memory(self):
        LibvirtXML.set_domain_memory(512, "KiB")
        assert "512" == LibvirtXML.domain_memory.text
        assert "KiB" == LibvirtXML.domain_memory.get("unit")

    def test_set_domain_memory_with_wrong_unit(self):
        with pytest.raises(exceptions.InvalidMemoryUnit):
            LibvirtXML.set_domain_memory(512, "test")

    def test_set_domain_vcpu(self):
        LibvirtXML.set_domain_vcpu(4)
        assert "4" == LibvirtXML.domain_vcpu.text

    def test_set_domain_vcpu_with_non_integers(self):
        with pytest.raises(ValueError):
            LibvirtXML.set_domain_vcpu("test")

    def test_set_domain_vcpu_auto_placement(self):
        LibvirtXML.set_domain_vcpu_auto_placement()
        assert "auto" == LibvirtXML.domain_vcpu.get("placement")

    def test_set_domain_vcpu_static_placement(self):
        LibvirtXML.set_domain_vcpu_static_placement("1")
        assert "1" == LibvirtXML.domain_vcpu.get("cpuset")

    def test_set_graphics(self):
        LibvirtXML.set_graphics("sdl",'-1', "yes")
        assert "sdl" == LibvirtXML.domain_devices_graphics.get("graphics_type")
        assert "-1" == LibvirtXML.domain_devices_graphics.get("port")  
        assert "yes" == LibvirtXML.domain_devices_graphics.get("autoport")   

    def test_set_graphics_with_wrong_unit(self):
        with pytest.raises(exceptions.InvalidGraphicsType):
            LibvirtXML.set_graphics("test",'-1', "yes") 

    def test_set_graphics_with_wrong_unit(self):
        with pytest.raises(exceptions.InvalidAutoPort):
            LibvirtXML.set_graphics("sdl",'-1', "test")  


    def test_set_domain_devices_disk_type_device(self):
        LibvirtXML.set_domain_devices_disk_type_device("file", "floppy")
        assert "file" == LibvirtXML.domain_devices_disk.get("type")
        assert "floppy" == LibvirtXML.domain_devices_disk.get("device") 

    def test_set_domain_devices_disk_type_device_with_wrong_unit(self):
        with pytest.raises(exceptions.InvalidDiskDevice):
            LibvirtXML.set_domain_devices_disk_type_device("file", "test") 

    def test_set_domain_devices_disk_type_device_with_wrong_unit(self):
        with pytest.raises(exceptions.InvalidDiskType):
            LibvirtXML.set_domain_devices_disk_type_device("test", "floppt") 

    def test_set_os_variant(self):
        LibvirtXML.set_os_variant('x86_64', "network")
        assert "x86_64" == LibvirtXML.domain_os_type.get("arch")
        assert "network" == LibvirtXML.domain_os_boot.get("dev") 

    def test_set_os_variant_with_wrong_unit(self):
        with pytest.raises(exceptions.InvalidBootDevType):
            LibvirtXML.set_os_variant("x86_64", "test")              
