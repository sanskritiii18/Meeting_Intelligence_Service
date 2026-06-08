from flask import Blueprint
from flask import request
from flask import jsonify

from auth.decorators import token_required
from services.action_item_service import ActionItemService

action_item_bp = Blueprint(
    "action_items",
    __name__,
    url_prefix="/api/action-items"
)

@action_item_bp.route(
    "",
    methods=["POST"]
)
@token_required
def create_action_item():

    data = request.get_json()

    response, status = (
        ActionItemService.create_action_item(data)
    )

    return jsonify(response), status


@action_item_bp.route(
    "/overdue",
    methods=["GET"]
)
@token_required
def get_overdue_action_items():

    response, status = (
        ActionItemService.get_overdue_action_items()
    )

    return jsonify(
        response
    ), status


@action_item_bp.route(
    "/<int:action_item_id>/status",
    methods=["PATCH"]
)
@token_required
def update_status(action_item_id):

    data = request.get_json()

    response, status = (
        ActionItemService.update_status(
            action_item_id,
            data
        )
    )

    return jsonify(response), status



@action_item_bp.route(
    "",
    methods=["GET"]
)
@token_required
def get_action_items():

    status = request.args.get(
        "status"
    )

    assignee = request.args.get(
        "assignee"
    )

    meeting_id = request.args.get(
        "meeting_id"
    )

    response, status_code = (
        ActionItemService.get_action_items(
            status,
            assignee,
            meeting_id
        )
    )

    return jsonify(
        response
    ), status_code