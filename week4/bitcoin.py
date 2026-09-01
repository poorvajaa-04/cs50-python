'''

In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. 
If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. 
You should replace YourApiKey with the actual API key you obtained from your CoinCap account dashboard, which returns a JSON object, 
among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:

import requests

try:
    ...
except requests.RequestException:
    ...

Outputs the current cost of n Bitcoins in USD to four decimal places, using , as a thousands separator.


'''

import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=82d7e1ad92df17ea14b45e88381523a3ff28de08a44b56344fca470c529f9bef"
    )
    data = response.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit("API request failed")

total = n * price

print(f"${total:,.4f}")