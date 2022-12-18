import requests
from bs4 import BeautifulSoup as bs


def get_amount(string):
    ok = True
    for char in string:
        if not (char.isdigit() or char == '.'):
            ok = False
            break
    if ok:
        return float(string)
    else:
        return None

    def getSoup():
        try:
            request = requests.get("https://www.banki.ru/products/currency/cb/")
            if request.status_code == 200:  # OK
                return bs(request.text, "html.parser")
            else:
                return None
        except Exception:
            return None
def main():
    currencies = ["USD", "EUR", "AUD", "CAD", "BYN", "KZT", "UAH", "GBP", "CZK", "CHF", "JPY"]
    info = "Supported currencies:"
    for currency in currencies:
        info += " " + currency
    print(info)

    amount = get_amount(input("Amount in rubles: "))
    if amount == None:
        print("Error: Wrong amount.")
        return

    currency = input("Сonvert to: ").upper()
    if currency not in currencies:
        print("Error: Unknown currency.")
        return

if __name__ == '__main__':
    main()