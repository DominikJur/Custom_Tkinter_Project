import requests


def check_connection_with_webservice_and_internet_connection():
    timeout = 5
    try:
        requests.get(
            "https://api.nbp.pl/api/exchangerates/tables/a/?format=json",
            timeout=timeout,
        )
    except Exception:
        try:
            requests.get("www.google.com", timeout=timeout)

            print(
                "Nie udało się pobrać danych, prawdodpodobnie brak połączenia z NBP. Wyliczenia na podstawie poprzednich kursów."
            )
            return False
        except Exception:
            print(
                "Nie udało się pobrać danych, prawdodpodobnie brak połączenia z internetem. Wyliczenia na podstawie poprzednich kursów."
            )
            return False
    return True
