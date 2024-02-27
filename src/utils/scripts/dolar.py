import logging
import os
import sys

from slack_sdk import WebClient

current_dir = os.path.dirname(os.path.abspath(__file__))

# Agrega la ruta del directorio "src" al sys.path
src_dir = os.path.join(current_dir, "../../../")
sys.path.append(src_dir)

# Ahora puedes importar el módulo "dolar_info_getter.py" correctamente
from src.utils.dolar_info_getter import get_dolar_info


CHANNEL='C05HL1ZCG5B'
logger = logging.basicConfig(level=logging.ERROR)

client = WebClient(
    token=os.environ.get('SLACK_BOT_TOKEN'),
    logger=logger
)

def parse_blocks():
    data = sorted( get_dolar_info(), key=lambda x: x['title'] )
    blocks = [
        {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"Valores por casa de cambio:"
			}
		},
		{
			"type": "divider"
		},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*\tCompra\t\tVenta\t\tCasa de Cambio*"
            }
        },
		{
			"type": "divider"
		}
    ]

    for element in data:
        message = f"*\t{ element['buy']['cost'] }{ set_trend( element['buy']['signal'] ) }\t{ element['sell']['cost'] }{ set_trend( element['sell']['signal'] ) }\t<{ element['site'] }|{ element['title'] }>*"
        blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": message 
                }
            }
        )
    
    return blocks


def set_trend(trend:str):
    if trend=='negative': return ":arrow_down_small:"
    elif trend=='positive': return ":arrow_up_small:"
    if trend=='equals': return ":heavy_equals_sign:"

client.chat_postMessage(
    channel=CHANNEL,
    blocks=parse_blocks()
)

command = {
    # 'token': '9wdhgiFpNVGV9NPzMY3auits', 
    'team_id': 'TFJ3PLTTM', 
    'team_domain': 'cweno', 
    'channel_id': 'C05HL1ZCG5B', 
    'channel_name': 'cambio_dolares', 
    'user_id': 'UFK8ELJGP', 
    'user_name': 'carlosbuenos', 
    # 'command': '/dolar', 
    # 'text': 'compra',
    # 'api_app_id': 'A05HQUGM8G0', 
    # 'is_enterprise_install': 'false', 
    'response_url': 'https://hooks.slack.com/commands/TFJ3PLTTM/5624971456512/I3N2wvM6dGxDwESDSHRx4aDl', 
    # 'trigger_id': '5586730795271.528125707939.bc9e8c8436b379a730daeefa4396750f'
}

context = {
    # 'is_enterprise_install': False, 
    'team_id': 'TFJ3PLTTM', 
    'user_id': 'UFK8ELJGP', 
    # 'actor_team_id': 'TFJ3PLTTM', 
    # 'actor_user_id': 'UFK8ELJGP', 
    'channel_id': 'C05HL1ZCG5B', 
    'response_url': 'https://hooks.slack.com/commands/TFJ3PLTTM/5624971456512/I3N2wvM6dGxDwESDSHRx4aDl', 
    # 'logger': "< Logger slack_bot.py (ERROR) >" , 
    'token': 'xoxb-528125707939-5581753156788-dMl3idUMHzTbtvX3SYv6cjlS', 
    # 'client': "< slack_sdk.web.client.WebClient object at 0x7f8c01460640 >" , 
    'authorize_result': {
        # 'enterprise_id': None, 
        # 'team_id': 'TFJ3PLTTM', 
        # 'team': None, 
        # 'url': None, 
        'bot_user_id': 'U05H3N54LP6', 
        'bot_id': 'B05GYB69NVB', 
        'bot_token': 'xoxb-528125707939-5581753156788-dMl3idUMHzTbtvX3SYv6cjlS', 
        # 'bot_scopes': None, 
        'user_id': 'UFK8ELJGP', 
        # 'user': None, 
        # 'user_token': None, 
        # 'user_scopes': None
    }, 
    'bot_id': 'B05GYB69NVB', 
    'bot_user_id': 'U05H3N54LP6', 
    'bot_token': 'xoxb-528125707939-5581753156788-dMl3idUMHzTbtvX3SYv6cjlS', 
    # 'ack': "< slack_bolt.context.ack.ack.Ack object at 0x7f8c01460730 >" , 
    # 'say': "< slack_bolt.context.say.say.Say object at 0x7f8c01460790 >" , 
    # 'respond': "< slack_bolt.context.respond.respond.Respond object at 0x7f8c014607f0 >" 
}

# dolares_callback(
#     command=command,
#     logger=Logger,
#     context=context
# )
