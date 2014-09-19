import requests
import json

def post_payload(uri, payload_dict):
    headers = {'content-type': 'application/json'}
    r = requests.post(uri, data=json.dumps(payload_dict), headers=headers)
    return payload_dict