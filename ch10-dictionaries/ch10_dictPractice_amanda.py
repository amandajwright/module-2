# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 13:39:02 2018

@author: 612436198
"""

#Practise with dict with function and subfun, variable, user inputs and if/else.

phoneBook_dict = {}

def phoneBook(phoneBook_dict):
    while len(phoneBook_dict.keys()) < 4:
        addToPhoneBook(phoneBook_dict)
    phoneBook_dict = phoneBookSort(phoneBook_dict)    
    return phoneBook_dict

def addToPhoneBook(phoneBook_dict):
    name = input("What is your name? ")
    lastThreePhone = int(input("What are the last three digits of your phone number? "))
    luckyNo = int(input("What is your lucky number? "))
    postCode = input("What is your postcode? ")
    town = input("What town or city do you live in? ")
    phoneBook_dict[name] = [lastThreePhone, luckyNo, postCode, town]
    phoneBook_dict[name].append(ageDiffFromQueen(phoneBook_dict))
    return phoneBook_dict

def phoneBookSort(phoneBook_dict):
    sortChoice = input("Would you like to sort the phone book by name (type 1), town (type 2), lucky number (type 3) or proximity to Queen's age (type 4)? ")
    if sortChoice == "1":
        sortedPhoneBook = sorted(phoneBook_dict.items())
    elif sortChoice == "2":
        sortedPhoneBook = sorted(phoneBook_dict.items(), key=lambda kv:kv[1][3])
    elif sortChoice == "3":
        sortedPhoneBook = sorted(phoneBook_dict.items(), key=lambda kv:kv[1][1])
    elif sortChoice == "4":
        sortedPhoneBook = sorted(phoneBook_dict.items(), key=lambda kv:kv[1][4])
    else:
        sortedPhoneBook = "Sorry, there was an error."
    return sortedPhoneBook

def ageDiffFromQueen(phoneBook_dict):
    age = int(input("How old are you? "))
    QueenAge = abs(92 - age)
    return QueenAge

def createDictFile(phoneBook_dict):
    file = open("phoneBookDict.txt", "w+")
    file.write(str(phoneBook_dict))
    file.close()
    
