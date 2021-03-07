import os, sys
from common import configuration


def app_dir():
    """Application data directory"""
    app_dir = os.path.abspath(os.path.pardir)
    return app_dir


def libvirt_dir():
    """Libvirt VM directory"""
    manager = configuration.ConfigManager()
    libvirt_dir = manager.get("GENERAL", "libvirt_directory")
    return libvirt_dir

def libvirt_images_dir():
    """ Libvirt Images directory  """
    manager = configuration.ConfigManager()
    libvirt_images_dir = manager.get("GENERAL", "libvirt_images_directory")
    return libvirt_dir

