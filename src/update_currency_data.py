import requests
import json
import sys


def update_currency_rates():  # Get currency info from NBP API
    sys.path.append("data")
    url = "https://api.nbp.pl/api/exchangerates/tables/a/?format=json"
    response = requests.get(url)
    r = [dict(response.json()[0])]
    r[0]["rates"].append(
        {
            "currency": "polski złoty",
            "code": "PLN",
            "mid": 1.0,
        }
    )

    with open("data/currency_data.json", "w") as file:
        json.dump(r, file)


if __name__ == "__main__":
    update_currency_rates()
