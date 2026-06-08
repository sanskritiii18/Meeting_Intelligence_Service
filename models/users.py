from database import db
from datetime import datetime

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(225),unique=True,nullable=False)
    password_hash = db.Column(db.Text,nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
