from marshmallow import Schema, fields, validate, post_load

from ...gen.model.Session import Session

class SessionSchema(Schema):
    price = fields.Str(required=True)
    days = fields.List(fields.Str(), required=True, validate=validate.Length(min=1))

    @post_load
    def make_session(self, data, **kwargs):
        return Session(**data)
