import requests

implementation = "Frankfurter" # alternatives: "Test"


def converti_frankfurter(importo, da="EUR", a="USD"):
    url = f"https://api.frankfurter.dev/v2/rates?quotes={da},{a}"
    response = requests.get(url)
    data = response.json()
    risultato = data[0]['rate']
    print(f"{importo} {da} = {risultato * importo}")

class ExchangeAPI:
    def find_exchange(self, from_currency, to_currency):
        pass

class ExchangeAPIFrankfurter(ExchangeAPI):
    def find_exchange(self, from_currency, to_currency):
        url = f"https://api.frankfurter.dev/v2/rates?quotes={from_currency},{to_currency}"
        response = requests.get(url)
        data = response.json()
        result = round(data[0]['rate'], 4)
        return result

class ExchangeAPITest(ExchangeAPI):
    def find_exchange(self, from_currency, to_currency):
        exchanges = {
            'USD': 1.16,
            "AUD": 1.8,
            "YEN": 10.5,
            "CHF": 0.89,
        }
        result = exchanges[from_currency]
        return result

class ExchangeAPIFactory():
    def create(self) -> ExchangeAPI:
        if implementation == "Frankfurter":
            return ExchangeAPIFrankfurter()
        elif implementation == "Test":
            return ExchangeAPITest()
        else:
            raise Exception(f"{implementation} non implemented!")

def set_implementation(name):
    global implementation
    implementation = name

if __name__ == "__main__":
    converti_frankfurter(100, "EUR", "USD")
