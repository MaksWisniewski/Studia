# Maksymilian Wiśniewski
# Part without api key 

import requests
from pprint import pprint


# Request dictionary is a function which for given word, calls api with requests module.
# then it is calling certain functions that are accesing the json file for specific parameters.

def request_dictionary(word="carte blanche"):
    # Prepare formated string for an api call.
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
  
    try:
        obj = requests.get(url).json()
    except:
        return

    pprint( get_definition(word, obj) )
    pprint( get_accent(word, obj))
    print()

def get_accent(word, json_obj):
    # in my opinion this api isn't standardized,
    # in order to omit errors i check if it's not valid entry 

    if json_obj[0].get("phonetic") is None:
        return ""
    else:
        return word + " is pronunced: " + json_obj[0]["phonetic"]

def get_definition(word, json_obj):
    return word + " means: " + json_obj[0]["meanings"][0]["definitions"][0]["definition"]


if __name__ == "__main__":
    request_dictionary()
    request_dictionary("polka")
    request_dictionary("Pneumonoultramicroscopicsilicovolcanoconiosis")
    request_dictionary("lad")
    request_dictionary("roadmen")
    request_dictionary("surveillance")
