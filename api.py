import requests

# Set the API endpoint URL
url = "https://api.binance.com/api/v3/account"

# Set the request headers
headers = {
    "X-MBX-APIKEY": "your-api-key"
}

# Send the request and get the response
response = requests.get(url, headers=headers)

# Print the response
print(response.json())
