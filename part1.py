def main():
    currencies = ["USD", "EUR", "AUD", "CAD", "BYN", "KZT", "UAH", "GBP", "CZK", "CHF", "JPY"]
    info = "Supported currencies:"
    for currency in currencies:
        info += " " + currency
    print(info)

if __name__ == '__main__':
    main()