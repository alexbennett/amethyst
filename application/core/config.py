import os
import json
import requests
from enum import Enum

# This file path
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

################
## Versioning ##
################

# Open version file
VERSION_FILE = open(os.path.join(__location__, '../../VERSION'))

# Get version number
VERSION = VERSION_FILE.read().strip()
