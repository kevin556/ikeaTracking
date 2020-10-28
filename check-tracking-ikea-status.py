#!/usr/local/bin/python3
import requests
import json
from config import *
from datetime import datetime

'''
    todo: add try catch and exception
    todo: add unit test
    todo: add list of tracking number
    todo: add gui
    todo: warn user by mail in order to be updated
'''

def get_data_from_post(url, headers, payload):
    res = requests.post(url, headers = headers, data= payload)
    return res

def get_current_time():
    return datetime.today().strftime('%Y-%m-%d-%H:%M:%S')


def write_to_a_file(data):
    filename = create_filename()
    with open(filename,'w') as f:
        f.write(get_current_time()+ ' -> ' + data)

def create_filename():
    return 'order_status_number_' + order_id + '_log.txt'

def create_url():
    return tracking_url +'/'+ order_id
    
def create_payload():
    return {'liteId': mail}

def create_headers():
    return {'accept-language': language}

def get_tracking_status(data):
    data = json.loads(data)
    current_status = data['order']['shipments'][0]['steps'][0]['status']
    write_to_a_file(current_status)
    print(current_status)

if __name__ == '__main__':
    payload = create_payload()
    headers = create_headers()
    url = create_url()
    data = get_data_from_post(url , headers, payload)
    get_tracking_status(data.text)
    