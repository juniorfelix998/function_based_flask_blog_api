from core.database import db
from posts.model import Posts
from core.base_schema import BaseSchema
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class PostSchema(BaseSchema):
    class Meta(ModelSchema.Meta):
        model = Posts
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    content = fields.String(required=True)

