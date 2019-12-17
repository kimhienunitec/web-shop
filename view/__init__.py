from flask import Flask


myapp = Flask(__name__, static_folder="../static", template_folder="../templates")
from view.account import *
from view.home import *
from view.admin import *