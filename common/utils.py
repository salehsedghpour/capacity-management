import os, sys


def app_dir():
    """Application data directory"""
    app_dir = os.path.abspath(os.path.pardir)
    return app_dir

