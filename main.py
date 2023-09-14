'''test requests'''
import requests
from pprint import pprint
url = 'https://randomuser.me/api/'
response = requests.get(url)

if response.status_code == 200:
    pprint(response.json())
else:
    pprint('some request errors')