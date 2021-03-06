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

