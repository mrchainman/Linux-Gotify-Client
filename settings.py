#!/usr/bin/python3
import requests
import json
import os
import time
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
from config import *
headers = {'X-Gotify-Key': token}
old = []
Notify.init("Gotify")
if not 'DISPLAY' in os.environ:
    os.environ['DISPLAY'] = ':0'
