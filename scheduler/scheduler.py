from apscheduler.schedulers.background import BackgroundScheduler

from scheduler.reminder_scheduler import send_reminders

def start_scheduler(app):

    scheduler = BackgroundScheduler()

    scheduler.add_job(
        func=lambda: send_reminders(app),
        trigger="interval",
        minutes=1
    )

    scheduler.start()