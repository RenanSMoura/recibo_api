from flask import request, jsonify
from flask_restful import Resource
from marshmallow import ValidationError

from ..controllers.ticket_controller import generate_ticket
from ..rest_api.schemas.user_schema import UserSchema


class GenerateTickedResource(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        user_schema = UserSchema()
        try:
            user = user_schema.load(json_data)
            data = generate_ticket(user)
        except ValidationError as err:
            return err.normalized_messages(), 400
        except BaseException as err:
            print(err)
            return err, 400

        return jsonify(json_data)
