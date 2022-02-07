import requests
import json2

def retrieve_messages(channelID):
    headers = {
        'authorization': 'ODI0OTU1NzQ2MjUyODgxOTgx.YgD5lg.n1iNJ_5lLN4RQTCuJoh2n0DbAVc'
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelID}/messages', headers=headers)
    output = json2.loads(r.text)
    for value in output:
            print(value['content'], '\n')

retrieve_messages('870343300761149502')

