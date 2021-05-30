from core.database import db
from core.base_model import BaseModel


class Posts(BaseModel):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    # user_id =
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
