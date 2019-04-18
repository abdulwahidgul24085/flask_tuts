from flask import Flask

app = Flask(__name__) # passes the flask class as a python predefined var.

from app import routes