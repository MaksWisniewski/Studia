import requests, json
from pprint import pprint

import private

def get_UserData(username="MaksWisniewski", url="https://api.github.com/users/"):
    return json.loads(requests.get(url+username).text)

def no_followers(username="MaksWisniewski"):
    return f"User: {username} has {get_UserData(username)['followers']} followers on github."

print(no_followers("mleczorsky"))
print(no_followers())


