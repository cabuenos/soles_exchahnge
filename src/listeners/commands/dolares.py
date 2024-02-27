import json

from logging import Logger
from decimal import Decimal

from utils.dolar_info_getter import get_dolar_info 
from ..templates import dolar_result
def dolares_callback(command, logger:Logger, context, ack, respond, say):
    ack()
    print('command')
    print(command)
    print('context')
    print(context)
    #
    # casos
    # /dolar compra/buy         muestra info de compra ordenada mayor-menor
    # /dolar venta/sell         muestra info de venta ordenada menor-mayor
    # /dolar ayuda/help/h       muestra ayuda
    # /dolar                    muestra info de compra y venta
    # #
    try:
        match command['text'].strip().lower():
            case 'buy' | 'compra':
                respond( response_buy_sell( command['text'], sort_info('buy', logger) ) )
            case 'sell' | 'venta':
                respond( response_buy_sell( command['text'], sort_info('sell', logger) ) )
            case 'h' | 'help' | 'ayuda':
                respond( response_help() )
            case '':
                respond( 'WIP' )
            case other:
                respond("No entendi, las opciones son 'Compra/Buy' y 'Venta/Sell' usa `/dolar ayuda` para ver las opciones")

    except Exception as ex:
        logger.error(ex)

def sort_info(movement:str, logger):
    try:
        exchange_data = sorted(
            get_dolar_info(),
            key=lambda x: Decimal( x[movement]['cost'] ),
            reverse=True if movement=='buy' else False
        )
        return [
            {
                "name": exh['title'],
                "link": exh['site'],
                "price": exh[movement]['cost'],
                "trend": set_trend(exh[movement]['signal']),
                "logo": exh['logo']
            } for exh in exchange_data
        ]

    except Exception as ex:
        logger.error(ex)

def set_trend(trend:str):
    if trend=='negative': return ":arrow_down_small:"
    elif trend=='positive': return ":arrow_up_small:"
    if trend=='equals': return ":heavy_equals_sign:"

def response_buy_sell(movement:str, data:list):
    blocks = [
        {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"Valores de {movement} al momento (de {'mayor a menor' if movement=='sell' else 'menor a mayor'}):"
			}
		},
		{
			"type": "divider"
		}
    ]
    
    for element in data:
        blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"\t{element['price']}\t{element['trend']}\t\t\t*<{element['link']}|{element['name']}>* "
                }
            }
        )

    return {'blocks': blocks}

def response_help():
    blocks = [
        {
            "type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"""
                Este comando verifica los valores de cambio para algunas casas de cambio\n
                Como usar:\n
                `/dolar compra`, `/dolar buy`         muestra info de compra ordenada mayor-menor\n
                `/dolar venta`, `/dolar sell`         muestra info de venta ordenada menor-mayor\n
                `/dolar ayuda`, `/dolar help`, `/dolar h`       muestra esta ayuda\n
                `/dolar`        muestra info de compra y venta
                """
			}
        }
    ]

    return {'blocks': blocks}

def response_all(data:list):
    pass



