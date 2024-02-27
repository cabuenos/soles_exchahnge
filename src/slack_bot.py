import os
import logging

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk.errors import SlackApiError

from listeners import register_listeners

load_dotenv()

logger = logging.basicConfig(level=logging.ERROR)

def initialize():
    try:
        return App(
            token= os.environ.get('SLACK_BOT_TOKEN')
        )
    except Exception as ex:
        print(ex)
    finally:
        pass

def start_bot():
    try:
        app = initialize()
        register_listeners(app)
        SocketModeHandler(
            app= app,
            app_token= os.environ.get('SLACK_SOCKET_APP_TOKEN')
        ).start()
    except Exception as ex: 
        print(ex)


# Start the bot
if __name__ == "__main__":
    start_bot()