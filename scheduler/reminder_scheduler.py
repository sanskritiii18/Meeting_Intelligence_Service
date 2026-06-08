from datetime import datetime

from database import db

from models.ActionItem import ActionItem
from models.reminder_history import ReminderHistory
def send_reminders(app):

    with app.app_context():

        overdue_items = ActionItem.query.filter(
            ActionItem.status != "COMPLETED",
            ActionItem.due_date < datetime.utcnow()
        ).all()

        for item in overdue_items:

            message = (
                f"Reminder: {item.task} "
                f"assigned to {item.assignee}"
            )

            history = ReminderHistory(
                action_item_id=item.id,
                message=message
            )

            db.session.add(history)

        db.session.commit()