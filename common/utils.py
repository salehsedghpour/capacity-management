import os, sys
from common.configuration import ConfigManager


def app_dir():
    """Application data directory"""
    app_dir = os.path.abspath(os.path.pardir)
    return app_dir


def libvirt_dir():
    """Libvirt VM directory"""
    manager = ConfigManager()
    libvirt_dir = manager.get("GENERAL", "libvirt_directory")
    return libvirt_dir