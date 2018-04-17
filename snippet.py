import requests

url = "http://158.69.254.209:8301/"

payload = ""
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'authorization': "Basic a2xhdHo6S0xa",
    'cache-control': "no-cache",
    'postman-token': "42898d50-035a-ea23-7df1-30e2cb381316"
    }

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)