# Description: Automate checking prices of crypto currencies
# Import modules/libraries

import datetime
# import client from coinbase
from coinbase.wallet.client import Client
# Store api key and api secret from coinbase.com/settings/api
user = Client(<api-key>, <api-secret>)
# Ask user what crypto currency he wants to know the price of 
input_text = "What cryptocurrency do you want to check on?\nEnter the in this format 'cryptocurrency-currency': "
while True:
    currency_pair = input(input_text)
    try:
        # Grab spot price of crypto currency from Coinbase
        # Returns a dictionari in the format:
        #{
        #"data": {
        #"amount": "1015.00",
        #"currency": "USD"
        #}
        #}
        price = user.get_spot_price(currency_pair=currency_pair.upper())
        # Store each value in a variable
        amount = price["amount"]
        base = price["base"]
        currency = price["currency"]
        # Display results
        print(f"The price of {base} in {currency} is: {amount} on {datetime.date.today()}. ")
        # Break while loop for correct user input
        break
    except:
        input_text = "Please enter the correct currency pair i.e. 'TheCryptoCurrency-TheCurrencyYouWantToConvertItTO': "
