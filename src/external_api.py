import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert(main_currency, conv_currency):
    """Получение курса валют из заданой валюты в RUB,"""

    if main_currency != conv_currency:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={main_currency}&from={conv_currency}&amount=1"

        payload = {}
        headers = {"apikey": API_KEY}

        response = requests.request("GET", url, headers=headers, data=payload)

        result = response.json()['result']
    else:
        result = 1
    return result
