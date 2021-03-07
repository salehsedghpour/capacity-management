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
