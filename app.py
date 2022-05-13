from flask import Flask

from .api.rest_api import init_app

def create_app():
    app = Flask(__name__)
    init_app(app)
    return app

