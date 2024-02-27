from slack_bolt import App
from .dolares import dolares_callback
from logging import Logger

def register(app:App):
    try:
        app.command('/dolar')(dolares_callback)
    except Exception as ex:
        Logger.error(ex)