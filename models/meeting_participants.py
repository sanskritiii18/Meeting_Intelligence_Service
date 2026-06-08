from database import db


class MeetingParticipant(db.Model):

    __tablename__ = "meeting_participants"

    id = db.Column(db.Integer,primary_key=True)

    meeting_id = db.Column(db.Integer,db.ForeignKey("meetings.id"),nullable=False)

    email = db.Column(db.String(255),nullable=False)