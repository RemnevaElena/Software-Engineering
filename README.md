Конвертирование рублей

Описание

Сервис по запросу пользователя, считывает актуальный курс валют на сайте и переводит сумму в рублях в иную валюту.

Запуск Docker

docker pull lenokvse0k/money
docker container run -it lenokvse0k/money

Тесты
- main [![Converter CI](https://github.com/RemnevaElena/Software-Engineering/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/RemnevaElena/Software-Engineering/actions/workflows/main.yml)

- develop [![Converter CI](https://github.com/RemnevaElena/Software-Engineering/actions/workflows/main.yml/badge.svg?branch=develop)](https://github.com/RemnevaElena/Software-Engineering/actions/workflows/main.yml)

Пример использования
1. После запуска программы в консоль выводится сообщение:
    Supported currencies: "USD", "EUR", "AUD", "CAD", "BYN", "KZT", "UAH", "GBP", "CZK", "CHF", "JPY"
    Amount in rubles:
2. Необходимо в строке "Amount in rubles:" записать число, например, 500
3. Далее на экране появится надпись: "Сonvert to:", ввести валюту, в которую собираемся переводить рубли, например,
    белорусские рубли, BYN
4. После на экране видим результат "Result: 19.76776825849915 BYN"
