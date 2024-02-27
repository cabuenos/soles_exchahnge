from logging import Logger
from ..templates import app_home
from slack_sdk import WebClient

def app_home_opened_callback(client:WebClient, event, logger:Logger, context, ack):
    if event['tab']=='home':
        try:        
            client.views_publish(
                user_id = event['user'],
                view=app_home
            )
        except Exception as ex:
            logger.error(ex)
    else: pass
