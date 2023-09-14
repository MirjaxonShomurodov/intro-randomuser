import requests
import json
from pprint import pprint
user_data = 'https://randomuser.me/api/'
url = 'https://randomuser.me/api/'

def get_user(user_data: dict) -> dict:
    '''get user from data
    
    Args:
        user_data (dict): user data from https://randomuser.me/api/
        
    Returns:
        dict: {
            'firstname': user firstname,
            'lastname': user lastname,
            'age': user age,
            'country': user country
        }
    '''
    m = {}
    response = requests.get(user_data).json()
    m["lastname"] = response["results"][0]["name"]["last"]
    m["age"] = response["results"][0]["dob"]["age"]
    m["country"] = response["results"][0]["location"]["country"]
    m["firstname"] = response['results'][0]["name"]["first"]
    return m
 
# data = get_user(user_data)
# pprint(data)

def get_users(url: str, n: int) -> list:
    '''get n users from url
    Args:
        url (str): api url
        n (int): number of users
        
    Returns:
        list: list of users. user from get_user()
    '''
    name = {}
    for i in range(n):
        get_users(url,1)
        response = requests.get(url).json()
        name["users"] = response["results"][0]["name"]["first"]
        return name["users"]
name = get_users(url,n=2)
print(name)
    

def write_users_to_file(file_path: str, n: int):
    '''write n users to file

    Args:
        url (str): api url
        n (int): number of users
    '''
    

