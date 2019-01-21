# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 10:11:31 2019

@author: amand
"""

import sqlite3
import json
import requests

conn = sqlite3.connect("phonebook.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS business(business_name TEXT, business_category TEXT, address1 TEXT, town_city TEXT, county TEXT, postcode TEXT, telephone_number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS person(surname TEXT, firstname TEXT, address1 TEXT, town_city TEXT, county TEXT, postcode TEXT, telephone_number TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS coordinate_mapping(town_city TEXT, postcode TEXT, x_coordinate REAL, y_coordinate REAL)")

#create_table()

#Realised (too late) the county column isn't useful/needed, so won't be used from now on.

person_file = open("json/mock_data_people_json.json")
person_data = json.load(person_file)

def dynamic_data_entry_person():
    for i in range(len(person_data)):
        surname = person_data[i]["last_name"]
        firstname = person_data[i]["first_name"]
        address1 = person_data[i]["address_line_1"]
        town_city = person_data[i]["address_line_2"]
        postcode = person_data[i]["postcode"]
        telephone_number = person_data[i]["telephone_number"]
        c.execute("INSERT INTO person(surname, firstname, address1, town_city, postcode, telephone_number) VALUES (?, ?, ?, ?, ?, ?)", (surname, firstname, address1, town_city, postcode, telephone_number))
        conn.commit()

business_file = open("json/mock_data_business_json.json")
business_data = json.load(business_file)

def dynamic_data_entry_business():
    for i in range(len(business_data)):
        business_name = business_data[i]["business name"]
        business_category = business_data[i]["business_category"]
        address1 = business_data[i]["address_line_1"]
        town_city = business_data[i]["address_line_2"]
        postcode = business_data[i]["postcode"]
        telephone_number = business_data[i]["telephone_number"]
        c.execute("INSERT INTO business(business_name, business_category, address1, town_city, postcode, telephone_number) VALUES (?, ?, ?, ?, ?, ?)", (business_name, business_category, address1, town_city, postcode, telephone_number))
        conn.commit()

#####USER INPUTS    

def phonebook():
    search_type = input("Search for person or business?\n")
    if search_type == "person":
        search_for_person()
    elif search_type == "business":
        search_for_business()
    else:
        print("Error.")
        return "Exit due to invalid response."
    
def search_for_person():
    inputPersonName = input("Please enter a name: ")
    location = input("Please enter the location: ")
    c.execute("SELECT * FROM person WHERE surname = ? AND postcode = ?", (inputPersonName, location))
    results = c.fetchall()
    if len(results) == 0:
        print("Sorry, nobody by that name exists in the database.")
    else:
        for row in results:
            print(row)

def search_for_business():
    searchChoice = input("Would you like to search by business name or business type?\n")
    if searchChoice == "name":
        print(business_by_name())
    elif searchChoice == "type":
        print(business_by_type())
    else:
        print("Error.")
        return "Exit due to invalid response."

def business_by_name():
    inputBusinessName = "Flashspan"
    location = "AB39 2ZH"
#    inputBusinessName = input("Please enter the name of the business you are looking for: ")
#    location = input("Please enter the location: ")
    c.execute("SELECT * FROM business WHERE business_name = ? AND postcode = ?", (inputBusinessName, location))
    results = c.fetchall()
    if len(results) == 0:
        return("Sorry, no business by that name exists in the database.")
    else:
        for i in range(len(results)):
            businesspostcode = results[i][5]
            c.execute("SELECT x_coordinate , y_coordinate FROM coordinate_mapping WHERE postcode = ?", (businesspostcode,))
            for row in c.fetchall():
                print(row)

def business_by_type():
    inputBusinessType = input("Please enter the type of business you are looking for: ")
    if include_location():
        location = input("Please enter the location: ")
        c.execute("SELECT * FROM business WHERE business_category = ? AND town_city = ? ORDER BY business_name", (inputBusinessType, location))
    else:
        c.execute("SELECT * FROM business WHERE business_category = ? ORDER BY business_name", (inputBusinessType,))
    if len(c.fetchall()) == 0:
        return("Sorry, no business of that type exists in the database.")
    else:
        for row in c.fetchall():
            return(row)

def include_location():
    locationChoice = input("Would you like to include a location in your search?\n")
    if locationChoice == "yes":
        return True
    elif locationChoice == "no":
        return False
    else:
        print("Error.")
        return "Exit due to invalid response."

### API stuff
def populateCoordTable():
     
    fourohfours = 0
    othererrors = 0
    
    for postcode in spacelessPostcodeList:
        postcode_response = requests.get(endpoint_postcode + postcode[2:-3])
        data_postcode = postcode_response.json()
        if data_postcode["status"] == 200:
            x_coordinate = data_postcode["result"]["latitude"]
            y_coordinate = data_postcode["result"]["longitude"]
            postcodefromapi = data_postcode["result"]["postcode"]
            c.execute("INSERT INTO coordinate_mapping(postcode, x_coordinate, y_coordinate) VALUES (?, ?, ?)", (postcodefromapi, x_coordinate, y_coordinate))
            conn.commit()
###TESTING
#    elif data_postcode["status"] == 404:
#        fourohfours += 1
#    else:
#        othererrors += 1
#print(fourohfours)
#print(othererrors)
            

        
