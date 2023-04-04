# Group Name: Paavo Nurmi (Gavin Reinhard, Sarah Ouellette, Zach Kelly, & Jakob Fisher)
# Email: ,,,fishe2jo@mail.uc.edu
# Assignment Title: Assignment 10
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: Main module that takes JSON from an API and returns interesting data.
# Citations: https://fdc.nal.usda.gov/api-guide.html Returns nutrition information for various food items.
# Anything else that's relevant: 
# main.py
import requests
import json

response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/list?api_key=Aflg26pw9eo9hsOT8tH4eJvgCXpMTZ4yfJ0xUOz3') # Make a request to a web server and store results in response.
json_string = response.content # Extract data from response and store in a string. 

#print(parsed_json[21]['description']) # Example for how to use the API, get rid of this before submitting. json_string needs to be parsed first.
