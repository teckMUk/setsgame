import os
from setuptools import setup

VERSION_FILE = open(os.path.join(".", ".version"))
VERSION = VERSION_FILE.read().strip()

setup(name="setgame", version=VERSION, packages=["setgame"], entry_points={"console_scripts": ["setgame = setgame.main:main"]})