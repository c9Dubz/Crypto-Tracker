# Description: Automate checking prices of crypto currencies
# Import modules/librairies
from selenium import webdriver
import datetime


# Selenium commands function to grab prices
def search(crypto):
    driver = webdriver.Chrome()
    driver.get('https://google.com')
    google_search = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
    google_search.send_keys(crypto)

    search_button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[3]/center/input[1]')
    search_button.click()

    crypto_price = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
    currency = driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[2]').text

    return crypto_price, currency


# Ask user what crypto currency he wants to enquire about
crypto_currency = input("What crypto currency do you want to check on? ")

# Try block to look for crypto price user needs
try:
    print(f"Checking {crypto_currency.upper()}'s price...")
    search(crypto_currency)
    crypto_price, currency = search(crypto_currency)
    print(f"{crypto_currency.upper()}'s Price: {crypto_price} in {currency} on {datetime.date.today()}.")
# Except block is information is missing or invalid input
except:
    print("There was an issue in completing your query.")

