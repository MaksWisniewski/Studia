# Maksymilian Wiśniewski

from pprint import pprint
import private
api_key = private.API_KEY


# import required modules
import requests, json

 
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 

def get_object(city_name): 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
 
    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    return response.json()
    
def get_weather(json_response):
    pprint( json_response["weather"][0] )

def print_info(city):
    pprint("Weather in " + city + " is: ")
    get_weather( get_object(city) )
    print("\n")

if __name__ == "__main__":
    print_info("wroclaw")
    print_info("Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch")