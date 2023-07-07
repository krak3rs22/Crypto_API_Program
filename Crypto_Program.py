import requests
from config import api_key

api = requests.get(api_key)
if api.ok:
    data = api.json()
    rates = data["rates"]

#  This function displays the currency value, if the value isn't found the program returns an according message
def display_currency_value():
    currency_name = input("Enter the name or symbol of the specific currency: ").upper()
    if currency_name in rates:
        print(f"{currency_name}: {rates[currency_name]} USD")
    else:
        print(f"The currency '{currency_name}' was not found.")

#  This function compares two cryptocurrencies, and also shows the difference between them, if the values aren't found the program returns an according message
def compare_currencies():
    currency_name1 = input("Enter the name or symbol of the first currency that will be compared: ").upper()
    currency_name2 = input("Enter the name or symbol of the second currency that will be compared: ").upper()
    if currency_name1 in rates and currency_name2 in rates:
        difference = rates[currency_name1] - rates[currency_name2]
        print(f"{currency_name1}: {rates[currency_name1]} USD; {currency_name2}: {rates[currency_name2]} USD; Difference: {difference:.5f} USD")
    else:
        if currency_name1 not in rates:
            print(f"The currency '{currency_name1}' does not exist.")
        if currency_name2 not in rates:
            print(f"The currency '{currency_name2}' does not exist.")

#  This function tracks the user's portfolio, calculating their money by multiplying the number of their specific cryptocurrencies by the amount of their specific cryptocurrency
def track_portfolio():
    portfolio = {}
    num_coins = int(input("Enter the number of coins in your portfolio: "))
    for i in range(num_coins):
        coin_name = input("Enter the name or symbol of the coin: ").upper()
        if coin_name in rates:
            coin_amount = float(input(f"Enter the amount of {coin_name}: "))
            portfolio[coin_name] = coin_amount
        else:
            print(f"The coin '{coin_name}' does not exist.")
    print("\nPortfolio Summary:")
    for coin_name, coin_amount in portfolio.items():
        coin_value = coin_amount * rates[coin_name]
        print(f"{coin_name}: {coin_value:.2f} USD")

#  This function notifies the user if a cryptocurrency has reached a certain value given by the user
def set_price_notifications():
    target_currency = input("Enter the name or symbol of the currency to set notifications for: ").upper()
    if target_currency in rates:
        target_price = float(input(f"Enter the target price for {target_currency}: "))
        while True:
            current_price = rates[target_currency]
            print(f"Current price for {target_currency}: {current_price} USD")
            if current_price >= target_price:
                print(f"Target price reached for {target_currency}!")
                # Send notification (like email.)
                break
            else:
                choice = input("Target price not reached. Check again? (Y/N): ")
                if choice.upper() == "N":
                    break
    else:
        print(f"The currency '{target_currency}' does not exist.")

#  Displays every currency in the API
def display_all_currencies():
    print("Available currencies:")
    for currency in rates:
        print(currency)

#  Converts the input currency into the output currency by multiplying the the amount of currency by the conversion rate
def currency_conversion():
    input_currency = input("Enter the name or symbol of the input currency: ").upper()
    output_currency = input("Enter the name or symbol of the output currency: ").upper()
    amount = float(input("Enter the amount of input currency: "))
    if input_currency in rates and output_currency in rates:
        conversion_rate = rates[output_currency] / rates[input_currency]
        converted_amount = amount * conversion_rate
        print(f"{amount} {input_currency} = {converted_amount} {output_currency}")
    else:
        if input_currency not in rates:
            print(f"The currency '{input_currency}' does not exist.")
        if output_currency not in rates:
            print(f"The currency '{output_currency}' does not exist.")

#  Main program
while True:
    print("----------------------------------------------------")
    user_input = input("Please enter a number into the program according to what you need.\n"
                       "[1] Look for a specific currency and display its current value.\n"
                       "[2] Compare prices between two different cryptocurrencies.\n"
                       "[3] Track your cryptocurrency portfolio.\n"
                       "[4] Set price notifications for a specific currency.\n"
                       "[5] Display all available currencies.\n"
                       "[6] Convert currencies.\n"
                       "[0] Exit the program.\n")
    if user_input == "1":
        display_currency_value()
    elif user_input == "2":
        compare_currencies()
    elif user_input == "3":
        track_portfolio()
    elif user_input == "4":
        set_price_notifications()
    elif user_input == "5":
        display_all_currencies()
    elif user_input == "6":
        currency_conversion()
    elif user_input == "0":
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please enter a valid option.")
