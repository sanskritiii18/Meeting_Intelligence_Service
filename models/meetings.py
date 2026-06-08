from datetime import datetime
from database import db


class Meeting(db.Model):

    __tablename__ = "meetings"

    id = db.Column(db.Integer,primary_key=True)

    title = db.Column(db.String(255),nullable=False)

    meeting_date = db.Column(db.DateTime,nullable=False)

    owner_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)

    created_at = db.Column(db.DateTime,default=datetime.utcnow)


    participants = db.relationship(
        "MeetingParticipant",
        backref="meeting",
        cascade="all, delete-orphan"
    )

    transcripts = db.relationship(
        "Transcript",
        backref="meeting",
        cascade="all, delete-orphan"
    )

