def get_amount(string):
    ok = True
    for char in string:
        if not (char.isdigit() or char == '.'):
            ok = False
            break
    if ok:
        return float(string)
    else:
        return None50
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

if __name__ == '__main__':
    main()