import os
from setuptools import setup

def find_packages(root):
    """Find all python packages that are in a subdirectory.
    """
    packages = []
    for dir, subdirs, files in os.walk(root):
        package = dir.replace(os.path.sep, '.')
        if '__init__.py' not in files:
            # not a package
            continue
        packages.append(package)
    return packages

setup(name='msmb',
      packages=find_packages('msmb'),
      scripts=['msmb/scripts/msmb']
      )