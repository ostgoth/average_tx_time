import http.client

conn = http.client.HTTPConnection("158.69.254.209:8301")

payload = ""

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'authorization': "Basic a2xhdHo6S0xa",
    'cache-control': "no-cache",
    'postman-token': "bac70e11-1c7f-97a7-cf7e-6c40bcf25e9b"
    }

conn.request("POST", "/", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))