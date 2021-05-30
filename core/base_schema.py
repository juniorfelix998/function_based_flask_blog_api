from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class BaseSchema(ModelSchema):
    created_at = fields.DateTime('%Y-%m-%d %H:%M:%S', dump_only=True)
    updated_at = fields.DateTime('%Y-%m-%d %H:%M:%S', dump_only=True)
