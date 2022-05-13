from marshmallow import Schema, fields, validate


class SessionSchema(Schema):
    session_price = fields.Int(required=True)
    session_days = fields.List(fields.Str(), required=True, validate=validate.Length(min=1))
