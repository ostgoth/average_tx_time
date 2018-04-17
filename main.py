import requests
import json
from requests.auth import HTTPBasicAuth


def get_block_time(block_hash):
    response1 = requests.post('http://158.69.254.209:8301', auth=HTTPBasicAuth('klatz', 'KLZ'),
                              json={"method": "getblock", "params": [block_hash], "id": 1})
    time_of_block = json.loads(response1.content)['result']['time']
    print('time of block ' + block_hash + ' is', time_of_block)
    return time_of_block
# get_block_time('00000000000002dfd23b17a642e2a17573c9e3ca91424c3d8b099234bd317d03')


def tx_count(block_hash):
    response3 = requests.post('http://158.69.254.209:8301', auth=HTTPBasicAuth('klatz', 'KLZ'),
                              json={"method": "getblock", "params": [block_hash], "id": 1})
    count = len(json.loads(response3.content)['result']['tx']) - 1
    print('tx count of ' + block_hash + ' is', count)
    return count
# tx_count('00000000000002dfd23b17a642e2a17573c9e3ca91424c3d8b099234bd317d03')


def get_previous_block_hash(block_hash):
    response2 = requests.post('http://158.69.254.209:8301', auth=HTTPBasicAuth('klatz', 'KLZ'),
                              json={"method": "getblock", "params": [block_hash], "id": 1})
    previous_hash = json.loads(response2.content)['result']['previousblockhash']
    print('previuos hash is:', previous_hash)
    return previous_hash
# get_previous_block_hash('0000000000000039ad1d4e6ce4d63f73601715e23be280a4886ef3336f3b5856')


response0 = requests.post('http://158.69.254.209:8301', auth=HTTPBasicAuth('klatz', 'KLZ'),
                          json={"method": "getblockchaininfo", "params": [], "id": 1})
block0 = json.loads(response0.content)['result']['bestblockhash']
i = 0
time_array = []
while i < 10:
    print('step %s: ' % i)
    i += 1
    block1 = get_previous_block_hash(block0)
    average_tx_block = (get_block_time(block0) - get_block_time(block1)) / tx_count(block0)
    time_array.append(average_tx_block)
    block0 = block1
print('time array:', time_array)
sum0 = 0
for i in time_array:
    sum0 += i
tx_average_time = sum0 / len(time_array)
tx_per_minute = 60 / tx_average_time
print('tx_per_minute= ', tx_per_minute)
