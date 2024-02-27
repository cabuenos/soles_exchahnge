from slack_bolt import App
from .app_home_opened import app_home_opened_callback
from logging import Logger

def register(app:App):
    try:
        app.event('app_home_opened')(app_home_opened_callback)
    except Exception as ex:
        Logger.error(ex)
