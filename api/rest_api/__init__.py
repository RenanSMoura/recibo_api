from flask import Blueprint
from flask_restful import Api

from .resources import GenerateTickedResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1/")
api = Api(bp)


def init_app(app):
    api.add_resource(GenerateTickedResource, "/ticket/")
    app.register_blueprint(bp)
