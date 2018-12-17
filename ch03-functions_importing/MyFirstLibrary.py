# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:46:07 2018

@author: 612436198
"""

def hello_world():
    print("Hello World!")

def initials():
    print("Please type your first name:")
    firstName = input()
    print("Please type your last name:")
    secondName = input()
    print("Your initials are: " + firstName[0] + secondName[0])

def myName():
    print("Amanda")
    print(2+2)

def secondMyName():
    print("What's your name?")
    myName = input()
    print(myName)

def secondHelloWorld():
    print("Hello World!")
    secondMyName()

def hello_world_2args(a, b):
    print("{} {}".format(a,b))

def hello_world_4args(a, b, c, d):
    print("{} {} {} {}".format(a,b,c,d))

def hello_world_8args(a, b, c, d, e, f, g, h):
    print("{0} {1}, if {2} {3} {4} {2} will {5} {6} {7}".format(a,b,c,d,e,f,g,h))

def say_this(a, b, c):
    print("{1} {0}, {2} {0}, ".format(a,b,c)*10)

def add_two_input_nos():
    print("Please type a number:")
    firstNumberTyped = input()
    print("Please type another number:")
    secondNumberTyped = input()
    print(int(firstNumberTyped) + int(secondNumberTyped))

def add_two_numbers():
    numberOne = 3
    numberTwo = 4
    answer = numberOne + numberTwo
    print(answer)

def add_two_numbers_from_args(a, b):
    print(a + b)

def convert_distance(miles):
    kilometers = (miles * 8.0) / 5.0
    return "Converting distance in miles to kilometers:\nDistance in miles: " + str(miles) + ";\nDistance in kilometers: " + str(kilometers) + "." 

def convert_distance_again(miles):
    kilometers = (miles * 8.0) / 5.0
    return "is " + str(miles) + "m, or " + str(kilometers) + "km."

Ipswich_to_London = convert_distance_again(10)
def distanceIpswichToLondon():
    return "The distance from Ipswich to London {}".format(Ipswich_to_London)

def convert_temperature(centigrade):
    fahrenheit = centigrade * 9.0 / 5.0 + 32
    kelvin = centigrade + 273.15
    return "That's " + str(fahrenheit) + " in fahrenheit and " + str(kelvin) + " in kelvin."

def temp_question():
    print("What temperature is it in centigrade?")
    tempOutside = int(input())
    return convert_temperature(tempOutside)

def ageRelativeToHRH():
    print("How old are you?")
    currentAge = int(input())
    if currentAge == 92:
        years = "You are the same age as the Queen!"
    elif currentAge > 92:
        years = "You are " + str(currentAge - 92) + " years older than the Queen."
    else:
        years = "You are " + str(92 - currentAge) + " years younger than the Queen."
    return years

def print_two(*args):
    arg1, arg2 = args
    print("arg1: {}, arg2: {}".format(arg1, arg2))
    
def print_two_again(arg1, arg2):
    print("arg1: {}, arg2: {}".format(arg1, arg2))
    
def print_one(arg1):
    print("arg1: {}".format(arg1))
    
def print_none():
    print("I got nothin'.")
    
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have {} cheeses!".format(cheese_count))
    print("You have {} boxes of crackers!".format(boxes_of_crackers))
    print("Man that's enought for a party!")
    print("Get a blanket.\n")

def christmasPresents(people, presents):
    print("There are {} people in my family.".format(people))
    print("They expect to receive {} presents each.".format(presents))
    print("Better get shopping!")

def peopleInFamily():
    parents = 2
    brothers = 2
    sisters_law = 2
    nieces_nephews = 3
    aunts_uncles = 3
    cousins = 2
    grandparents = 1
    return parents + brothers + sisters_law + nieces_nephews + aunts_uncles + cousins + grandparents

def presentsExpectedByEach():
    return 2

def christmasPresentsSpecific():
    christmasPresents(15,2)

def christmasPresentsSpecificAgain():
    people = 7
    presents = 3
    return christmasPresents(people, presents)
