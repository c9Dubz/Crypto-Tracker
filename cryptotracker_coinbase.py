import datetime
from coinbase.wallet.client import Client

user = Client(<api-key>, <api-secret>)
input_text = "What cryptocurrency do you want to check on?\nEnter the in this format 'cryptocurrency-currency': "
while True:
    currency_pair = input(input_text)
    try:
        price = user.get_spot_price(currency_pair=currency_pair.upper())

        amount = price["amount"]
        base = price["base"]
        currency = price["currency"]

        print(f"The price of {base} in {currency} is: {amount} on {datetime.date.today()}. ")
        break

    except:
        input_text = "Please enter the correct currency pair i.e. 'TheCryptoCurrency-TheCurrencyYouWantToConvertItTO': "



