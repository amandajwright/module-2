# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:03:48 2019

@author: 612436198
"""

#Task 1: Mailgun.

import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxc71cd092ea784f188f746e55315641de.mailgun.org/messages",
        auth=("api", "-apikey-"),
        data={"from": "Excited User <amanda.jane.wright@gmail.com>",
              "to": ["amanda.2.wright@bt.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
    
send_simple_message()

#Task 2: A weather app.

import requests

endpoint = "http://api.openweathermap.org/data/2.5/weather"

payload = {"q": "London,UK", "units":"metric", "appid":"849babde6cea7947bb9798ad7dd83f4d"}

response = requests.get(endpoint, params=payload)

#print(response.url)
#print(response.status_code)
#print(response.headers["content-type"])

data = response.json()

print(data)