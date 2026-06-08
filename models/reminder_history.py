from datetime import datetime

from database import db


class ReminderHistory(db.Model):

    __tablename__ = "reminder_history"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    action_item_id = db.Column(
        db.Integer,
        db.ForeignKey("action_items.id"),
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    sent_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )