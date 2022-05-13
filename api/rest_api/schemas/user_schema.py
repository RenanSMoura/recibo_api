from marshmallow import Schema,fields, validate, post_load

from ..schemas.session_schema import SessionSchema
from ...gen.model.User import User


class UserSchema(Schema):
    title = fields.Str(validate=validate.OneOf(["Sra", "Sr"]), required=True)
    name = fields.Str(required=True)
    payment_day = fields.DateTime(required=True, format="iso")
    email = fields.Email()
    session = fields.Nested(SessionSchema)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
