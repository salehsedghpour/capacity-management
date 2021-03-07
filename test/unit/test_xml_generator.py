import pytest

from common.configuration import LibvirtXMLGenerator
from common import exceptions


LibvirtXML = LibvirtXMLGenerator()


class TestLibvirtXMLGenerator(object):
    def test_set_domain_type(self):
        LibvirtXML.set_domain_type("kvm")
        assert "kvm" == LibvirtXML.domain.get("type")

    def test_set_domain_type_error(self):
        with pytest.raises(exceptions.InvalidDomainType):
            LibvirtXML.set_domain_type("test")

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

    def test_set_domain_vcpu_placement(self):
        LibvirtXML.set_domain_vcpu_placement("auto")
        assert "auto" == LibvirtXML.domain_vcpu.get("placement")

    def test_set_domain_vcpu_placement_cpuset(self):
        LibvirtXML.set_domain_vcpu_placement("static", "1")
        assert "1" == LibvirtXML.domain_vcpu.get("cpuset")

    def test_set_domain_vcpu_placement_with_wrnong_placement(self):
        with pytest.raises(exceptions.InvalidVCPUPlacement):
            LibvirtXML.set_domain_vcpu_placement("test")

    def test_set_graphics(self):
        LibvirtXML.set_graphics("sdl",'-1', "yes")
        assert "sdl" == LibvirtXML.domain_devices_graphics.get("graphics_type")
        assert "-1" == LibvirtXML.domain_devices_graphics.get("port")  
        assert "yes" == LibvirtXML.domain_devices_graphics.get("autoport")         