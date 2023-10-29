from apscheduler.schedulers.background import BackgroundScheduler
from app.scheduler.tasks import delete_news_nextday


scheduler = BackgroundScheduler()

scheduler.add_job(delete_news_nextday, "cron", hour=0, minute=0, second=0)