"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import Flask_Login.views
import jinja2.ext
