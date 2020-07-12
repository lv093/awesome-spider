from flask import current_app
from flask_apscheduler import APScheduler


class Scheduler(APScheduler):

    def get_app(self):
        if self.app:
            return self.app
        if current_app:
            return current_app


scheduler = Scheduler()
