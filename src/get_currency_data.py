from .check_connection import check_connection_with_webservice_and_internet_connection
from .update_currency_data import update_currency_rates
import json
import sys


def get_currency_rates():
    sys.path.append("data")
    if check_connection_with_webservice_and_internet_connection():
        update_currency_rates()
    with open("data/currency_data.json", "r") as file:
        return json.load(file)
