# 2/3. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp

# импорт всего нужного
import requests
from datetime import datetime
from decimal import *

# выбор точности, кол-во знаков после запятой
getcontext().prec = 4


# функция
def currency_rates(currency):
    currency = currency.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if currency not in response:
        return None

    ex_curr = response[response.find('<Value>', response.find(currency)) +
                       7:response.find('</Value>', response.find(currency))]
    day_raw = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, day_raw)
    return f"{Decimal(ex_curr.replace(',', '.'))}, {datetime(day=day, month=month, year=year)}"


if __name__ == '__main__':
    curr = input('Введите валюту: ')
    print(currency_rates(curr))
