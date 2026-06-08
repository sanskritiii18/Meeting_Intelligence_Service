from datetime import datetime
from database import db
from models.meetings import Meeting
from models.meeting_participants import MeetingParticipant
from models.transcripts import Transcript
from services.ai_service import AIService


class MeetingService:

    @staticmethod
    def create_meeting(data, owner_id):

        title = data.get("title")
        participants = data.get("participants", [])
        meeting_date = data.get("meetingDate")
        transcript = data.get("transcript", [])

        if not title:
            return {
                "success": False,
                "message": "Meeting title is required"
            }, 400

        if not meeting_date:
            return {
                "success": False,
                "message": "Meeting date is required"
            }, 400

        meeting = Meeting(
            title=title,
            meeting_date=datetime.fromisoformat(
                meeting_date.replace("Z", "+00:00")
            ),
            owner_id=owner_id
        )

        db.session.add(meeting)
        db.session.flush()

        for email in participants:

            participant = MeetingParticipant(
                meeting_id=meeting.id,
                email=email
            )

            db.session.add(participant)

        for item in transcript:

            transcript_entry = Transcript(
                meeting_id=meeting.id,
                timestamp=item["timestamp"],
                speaker=item["speaker"],
                text=item["text"]
            )

            db.session.add(transcript_entry)

        db.session.commit()

        return {
            "success": True,
            "message": "Meeting created successfully",
            "meeting_id": meeting.id
        }, 201

    @staticmethod
    def get_meeting_by_id(meeting_id, owner_id):

        meeting = Meeting.query.filter_by(
            id=meeting_id,
            owner_id=owner_id
        ).first()

        if not meeting:

            return {
                "success": False,
                "message": "Meeting not found"
            }, 404

        participants = []

        for participant in meeting.participants:

            participants.append(
                participant.email
            )

        transcript = []

        for item in meeting.transcripts:

            transcript.append({
                "timestamp": item.timestamp,
                "speaker": item.speaker,
                "text": item.text
            })

        return {
            "success": True,
            "data": {
                "id": meeting.id,
                "title": meeting.title,
                "meetingDate": meeting.meeting_date,
                "participants": participants,
                "transcript": transcript
            }
        }, 200

    @staticmethod
    def list_meetings(owner_id, page, limit):

        query = Meeting.query.filter_by(
            owner_id=owner_id
        )

        total = query.count()

        meetings = query.offset(
            (page - 1) * limit
        ).limit(limit).all()

        result = []

        for meeting in meetings:

            result.append({
                "id": meeting.id,
                "title": meeting.title,
                "meetingDate": meeting.meeting_date
            })

        return {
            "success": True,
            "page": page,
            "limit": limit,
            "total": total,
            "data": result
        }, 200

    @staticmethod
    def analyze_meeting(
            meeting_id,
            owner_id
    ):

        meeting = Meeting.query.filter_by(
            id=meeting_id,
            owner_id=owner_id
        ).first()

        if not meeting:
            return {
                "success": False,
                "message": "Meeting not found"
            }, 404

        transcripts = Transcript.query.filter_by(
            meeting_id=meeting.id
        ).all()

        transcript_text = ""

        for row in transcripts:
            transcript_text += (
                f"[{row.timestamp}] "
                f"{row.speaker}: "
                f"{row.text}\n"
            )

        analysis = AIService.analyze_transcript(
            transcript_text
        )

        return {
            "success": True,
            "data": analysis
        }, 200
