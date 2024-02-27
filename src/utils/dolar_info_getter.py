from bs4 import BeautifulSoup
import requests, json

def __get_data():
    url='https://cuantoestaeldolar.pe/'
    response = requests.get(url=url)

    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('script', id='__NEXT_DATA__')
    return json.loads(data.text)

def get_dolar_info():
    info = __get_data()
    base = info['props']['pageProps']
    houses_data = base['onlineExchangeHouses']
    houses_data.append(base['houseOnly'])
    houses_info= [
        {
            'id' : house['id'],
            'title' : house['title'],
            'site' : house['site'].split('?')[0],
            'buy' : house['rates']['buy'],
            'sell' : house['rates']['sale'],
            'bank' : house['bank'],
            'logo' : f'https://cuantoestaeldolar.pe/{house["img"]}'
        } for house in houses_data
        if 'BCP' in house['bank']
    ]
    
    return houses_info

get_dolar_info()