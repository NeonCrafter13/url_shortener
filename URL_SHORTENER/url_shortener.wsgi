#!/usr/bin/python
import sys

activate_this = '/var/www/html/URL_SHORTENER/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

sys.path.insert(0, "/var/www/html/URL_SHORTENER")
from app import app as application
