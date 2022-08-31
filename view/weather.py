import requests
from bs4 import BeautifulSoup as bs


def get_data():
    r = requests.get(
        'https://www.yandex.com/weather/segment/details?offset=0&lat=55.753215&lon=37.622504&geoid=213',
        headers={'User-Agent': 'Mozilla/5.0'})
    soup = bs(r.content, 'html.parser')

    res = list()
    for card in soup.select('.card:not(.adv)'):
        # date = ' '.join([i.text for i in card.select('[class$=number],[class$=month]')])
        temps = list(zip(
            [i.text for i in card.select('.weather-table__daypart')]
            , [i.text for i in card.select('.weather-table__body-cell_type_daypart .temp__value')]
        ))
        if len(temps) > 0:
            res.append(temps)
    return res


def get_weather(day=0):
    data = get_data()
    if not (0 <= day < len(data)):
        raise Exception
    day_data = [int(temp[1].replace("−", "-")) for temp in data[day]]
    return day_data


def get_weather_average(day=0):
    data = get_weather(day)
    return sum(data) / len(data)
