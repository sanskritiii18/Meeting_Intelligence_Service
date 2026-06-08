from database import db


class Transcript(db.Model):

    __tablename__ = "transcripts"

    id = db.Column(db.Integer,primary_key=True)

    meeting_id = db.Column(db.Integer,db.ForeignKey("meetings.id"),nullable=False)

    timestamp = db.Column(db.String(20),nullable=False)

    speaker = db.Column(db.String(100),nullable=False)

    text = db.Column(db.Text,nullable=False)