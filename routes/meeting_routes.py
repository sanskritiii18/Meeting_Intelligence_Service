from flask import Blueprint
from flask import request
from flask import jsonify
from flask import g

from auth.decorators import token_required
from services.meeting_service import MeetingService


meeting_bp = Blueprint(
    "meetings",
    __name__,
    url_prefix="/meetings"
)


@meeting_bp.route(
    "",
    methods=["POST"]
)
@token_required
def create_meeting():

    data = request.get_json()

    response, status = (
        MeetingService.create_meeting(
            data,
            g.current_user.id
        )
    )

    return jsonify(response), status


@meeting_bp.route(
    "/<int:meeting_id>",
    methods=["GET"]
)
@token_required
def get_meeting(meeting_id):

    response, status = (
        MeetingService.get_meeting_by_id(
            meeting_id,
            g.current_user.id
        )
    )

    return jsonify(response), status


@meeting_bp.route(
    "",
    methods=["GET"]
)
@token_required
def list_meetings():

    page = int(
        request.args.get(
            "page",
            1
        )
    )

    limit = int(
        request.args.get(
            "limit",
            10
        )
    )

    response, status = (
        MeetingService.list_meetings(
            g.current_user.id,
            page,
            limit
        )
    )

    return jsonify(response), status


@meeting_bp.route(
    "/<int:meeting_id>/analyze",
    methods=["POST"]
)
@token_required
def analyze_meeting(meeting_id):

    response, status = (
        MeetingService.analyze_meeting(
            meeting_id,
            g.current_user.id
        )
    )

    return jsonify(response), status