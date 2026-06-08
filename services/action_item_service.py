from datetime import datetime

from database import db
from models.ActionItem import ActionItem


class ActionItemService:

    @staticmethod
    def create_action_item(data):

        meeting_id = data.get("meeting_id")
        task = data.get("task")
        assignee = data.get("assignee")
        due_date = data.get("due_date")

        if not meeting_id:
            return {
                "success": False,
                "message": "meeting_id is required"
            }, 400

        if not task:
            return {
                "success": False,
                "message": "task is required"
            }, 400

        if not assignee:
            return {
                "success": False,
                "message": "assignee is required"
            }, 400

        if not due_date:
            return {
                "success": False,
                "message": "due_date is required"
            }, 400

        action_item = ActionItem(
            meeting_id=meeting_id,
            task=task,
            assignee=assignee,
            due_date=datetime.fromisoformat(
                due_date.replace("Z", "+00:00")
            )
        )

        db.session.add(action_item)
        db.session.commit()

        return {
            "success": True,
            "message": "Action item created",
            "action_item_id": action_item.id
        }, 201

    @staticmethod
    def update_status(
            action_item_id,
            data
    ):

        action_item = ActionItem.query.get(
            action_item_id
        )

        if not action_item:
            return {
                "success": False,
                "message": "Action item not found"
            }, 404

        status = data.get("status")

        allowed_statuses = [
            "PENDING",
            "IN_PROGRESS",
            "COMPLETED"
        ]

        if status not in allowed_statuses:
            return {
                "success": False,
                "message": "Invalid status"
            }, 400

        action_item.status = status

        db.session.commit()

        return {
            "success": True,
            "message": "Status updated successfully"
        }, 200

    @staticmethod
    def get_action_items(
            status=None,
            assignee=None,
            meeting_id=None
    ):

        query = ActionItem.query

        if status:
            query = query.filter(
                ActionItem.status == status
            )

        if assignee:
            query = query.filter(
                ActionItem.assignee == assignee
            )

        if meeting_id:
            query = query.filter(
                ActionItem.meeting_id == meeting_id
            )

        action_items = query.all()

        result = []

        for item in action_items:
            result.append({
                "id": item.id,
                "meeting_id": item.meeting_id,
                "task": item.task,
                "assignee": item.assignee,
                "status": item.status,
                "due_date": item.due_date
            })

        return {
            "success": True,
            "data": result
        }, 200

    @staticmethod
    def get_overdue_action_items():

        overdue_items = ActionItem.query.filter(
            ActionItem.status != "COMPLETED",
            ActionItem.due_date < datetime.utcnow()
        ).all()

        result = []

        for item in overdue_items:
            result.append({
                "id": item.id,
                "meeting_id": item.meeting_id,
                "task": item.task,
                "assignee": item.assignee,
                "status": item.status,
                "due_date": item.due_date
            })

        return {
            "success": True,
            "data": result
        }, 200