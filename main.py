import requests
import json
from requests.auth import HTTPBasicAuth

"""
curl 158.69.254.209:8301 -s -X POST -H "Content-Type: application/json" -H "Authorization: Basic a2xhdHo6S0xa" --data
 '{"method":"getblockchaininfo","params":[],"id":1}' | json_pp
 
curl -u klatz:KLZ http://158.69.254.209:8301 -s -X POST -H "Content-Type: application/json" --data 
 '{"method":"getblockchaininfo","params":[],"id":1}' | json_pp
 
curl 158.69.254.209:8301 -s -X POST -H "Content-Type: application/json" -H "Authorization: Basic a2xhdHo6S0xa" --data
 '{"method":"getblock","params":["00000000000002dfd23b17a642e2a17573c9e3ca91424c3d8b099234bd317d03"],"id":1}' | json_pp
  
curl -u klatz:KLZ 158.69.254.209:8301 -s -X POST -H "Content-Type: application/json" --data
 '{"method":"getblock","params":["00000000000002dfd23b17a642e2a17573c9e3ca91424c3d8b099234bd317d03"],"id":1}' | json_pp
"""
"""
r = requests.post('http://158.69.254.209:8301', auth=HTTPBasicAuth('klatz', 'KLZ'),
                  json={"method": "getblockchaininfo", "params": [], "id": 1})
print('getblockchaininfo response: ', r.content)

j = json.loads(r.content)
print('bestblockhash: ', j['result']['bestblockhash'])

r1 = requests.post('http://158.69.254.209:8301', auth=HTTPBasicAuth('klatz', 'KLZ'),
                  json={"method": "getblock", "params": [j['result']['bestblockhash']], "id": 1})
print('getblock response: ', r1.content)
j1 = json.loads(r1.content)
print('block time: ', j1['result']['time'])
print('previousblockhash: ', j1['result']['previousblockhash'])
print(len(j1['result']['tx'])-1)
"""

def get_block_time(block_hash):
    r1 = requests.post('http://158.69.254.209:8301', auth=HTTPBasicAuth('klatz', 'KLZ'),
                       json={"method": "getblock", "params":[block_hash], "id": 1})
    time_of_block = json.loads(r1.content)['result']['time']
    print('time of block ' + block_hash + ' is', time_of_block)
    return time_of_block

get_block_time('00000000000002dfd23b17a642e2a17573c9e3ca91424c3d8b099234bd317d03')


"""

block0 = j['result']['bestblockhash']
block1 = j1['result']['previousblockhash']
i = 0
while i<10:
    i+= 1

#    print('step %s: ' %i)
"""