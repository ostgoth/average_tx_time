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
    response1 = requests.post('http://158.69.254.209:8301', auth=HTTPBasicAuth('klatz', 'KLZ'),
                       json={"method": "getblock", "params":[block_hash], "id": 1})
    time_of_block = json.loads(response1.content)['result']['time']
    print('time of block ' + block_hash + ' is', time_of_block)
    return time_of_block
#get_block_time('00000000000002dfd23b17a642e2a17573c9e3ca91424c3d8b099234bd317d03')

def tx_count(block_hash):
    response3 = requests.post('http://158.69.254.209:8301', auth=HTTPBasicAuth('klatz', 'KLZ'),
                       json={"method": "getblock", "params":[block_hash], "id": 1})
    count = len(json.loads(response3.content)['result']['tx']) - 1
    print('tx count of ' + block_hash + ' is', count)
    return count
#tx_count('00000000000002dfd23b17a642e2a17573c9e3ca91424c3d8b099234bd317d03')

def get_previous_block_hash(block_hash):
    response2 = requests.post('http://158.69.254.209:8301', auth=HTTPBasicAuth('klatz', 'KLZ'),
                              json={"method": "getblock", "params": [block_hash], "id": 1})
    previous_hash = json.loads(response2.content)['result']['previousblockhash']
    print('previuos hash is:', previous_hash)
    return previous_hash
#get_previous_block_hash('0000000000000039ad1d4e6ce4d63f73601715e23be280a4886ef3336f3b5856')

response0 = requests.post('http://158.69.254.209:8301', auth=HTTPBasicAuth('klatz', 'KLZ'),
                  json={"method": "getblockchaininfo", "params": [], "id": 1})
block0 = json.loads(response0.content)['result']['bestblockhash']
i = 0
time_array = []
while i<10:
    print('step %s: ' % i)
    i+= 1
    block1 = get_previous_block_hash(block0)
    average_tx_block = (get_block_time(block0) - get_block_time(block1)) / tx_count(block0)
    time_array.append(average_tx_block)
    block0 = block1
print('time array:', time_array)
for i in time_array:
    sum += time_array[i]
tx_average_time = sum / len(time_array)
print('tx_average_time = ', tx_average_time)



