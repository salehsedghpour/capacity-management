import pytest

from common.configuration import LibvirtXMLGenerator


LibvirtXML = LibvirtXMLGenerator()


class TestLibvirtXMLGenerator(object):
    def test_set_domain_type(self):
        LibvirtXML.set_domain_type("kvm")
        assert "kvm" == LibvirtXML.domain.get("type")
