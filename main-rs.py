import requests
from requests.auth import HTTPBasicAuth

"""
curl 158.69.254.209:8301 -s -X POST -H "Content-Type: application/json" -H "Authorization: Basic a2xhdHo6S0xa" --data
 '{"method":"getblockchaininfo","params":[],"id":1}' | json_pp

 curl -u klatz:KLZ http://158.69.254.209:8301 -s -X POST -H "Content-Type: application/json" --data 
 '{"method":"getblockchaininfo","params":[],"id":1}' | json_pp
 """

payload = (('method', 'getblockchaininfo'), ('params', []), ('id', 1))
r = requests.post('http://158.69.254.209:8301', auth=HTTPBasicAuth('klatz', 'KLZ'), data=payload)
print(r.content)



"""
targetws = 'https://secure.advfn.com/login/secure'

s = requests.session()

payload_data = {'login_username': 'xxx', 'login_password': 'yyy'}

response = s.post(targetws, data=payload_data)


url='https://it.advfn.com/mercati/BIT/generali-G/ordini'

result = s.get(url)

print result.content
"""