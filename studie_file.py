import requests

print("Python")

# Coin name that we need to obtain information
# We will use interpolation method with URL
coin = "bitcoin"

# API URL
url = f"https://api.coingecko.com/api/v3/coins/{coin}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
#       print(data)
#       print(data.keys())
    print(data["market_data"]["current_price"]["usd"])

    for coin in data["market_data"]["current_price"]:
        print(f"{coin} {data['market_data']['current_price'][coin]} bitcoins")

else:
    print("Error to obtain data from API", response.status_code)

