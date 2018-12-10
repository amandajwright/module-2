# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:55:59 2018

@author: 612436198
"""
#
##Different ways of having a person answer a question and using the answer.
##Also the different ways of applying the title function to the answer.
#print("What's your name?")
#name = input()
#print("Hello {}!".format(name.title()))
#
#print("What's your last name?")
#name = input().title()
#print("Hey {}.".format(name))
#
#name = input("What's your name? ")
#name = name.title()
#print("Hello {}!".format(name))
#
##Just asking someone a question and storing their answer as a variable.
#age = input("Please type your age: ")
#
##Using input and format functions together.
#print("What's your first name?")
#firstName = input().title()
#print("What's your last name?")
#lastName = input().title()
#print("Hello {} {}!".format(firstName,lastName))
#
##Using input and format functions together retrieving more than one piece of info from one answer.
#print("Please type your name and where you're from separated by a comma.")
#namePlace = input()
#namePlaceList = namePlace.split(",")
#print("Hello {} from {}.".format(namePlaceList[0], namePlaceList[1]))
#
##Writing your first function.
#def hello_world():
#    print("Hello World!")
#
##Calling your first function.    
#hello_world()
#
##Test function
#def initials():
#    print("Please type your first name:")
#    firstName = input()
#    print("Please type your last name:")
#    secondName = input()
#    print("Your initials are: " + firstName[0] + secondName[0])
#    
#initials()
#
#
##Task2 from lecture slides.
##Task2(1), (2)
#def myName():
#    print("Amanda")
#    print(2+2)
#
#myName()
#
##Task2(3)    
#def secondMyName():
#    print("What's your name?")
#    myName = input()
#    print(myName)
#    
#secondMyName()
#
##Task2 Challenge
#def secondHelloWorld():
#    print("Hello World!")
#    secondMyName()
#
#secondHelloWorld()
#
##Task2_2
#def hello_world_2args(a, b):
#    print("{} {}".format(a,b))
#    
#a1 = "hello"
#b1 = "world"
#a2 = "love"
#b2 = "coding"
#
#hello_world_2args(a1, b1)
#
#hello_world_2args(a2, b2)
#
#def hello_world_4args(a, b, c, d):
#    print("{} {} {} {}".format(a,b,c,d))
#
#a3 = "have"
#b3 = "happy week!"
#a4 = "a"
#
#hello_world_4args(a1, a3, a4, b3)
#
#def hello_world_8args(a, b, c, d, e, f, g, h):
#    print("{0} {1}, if {2} {3} {4} {2} will {5} {6} {7}".format(a,b,c,d,e,f,g,h))
#
#b4 = "you"
#
#hello_world_8args(a1, b1, b4, a2, b2, a3, a4, b3)
#
#def say_this(a, b, c):
#    print("{1} {0}, {2} {0}, ".format(a,b,c)*10)
#
#noun = "lorry"
#colourOne = "red"
#colourTwo = "yellow"
#
#say_this(noun, colourOne, colourTwo)
#
##Functions with different numbers of arguments.
#print(list(range(10)))
#print(list(range(1,10)))
#print(list(range(1,10,2)))
#
##Adding two inputted numbers
#def add_two_input_nos():
#    print("Please type a number:")
#    firstNumberTyped = input()
#    print("Please type another number:")
#    secondNumberTyped = input()
#    print(int(firstNumberTyped) + int(secondNumberTyped))
#    
#add_two_input_nos()
#
##Task 3
#def add_two_numbers():
#    numberOne = 3
#    numberTwo = 4
#    answer = numberOne + numberTwo
#    print(answer)
#    
#add_two_numbers()
#
#def add_two_numbers_from_args(a, b):
#    print(a + b)
#
#firstNumber = 1
#secondNumber = 2
#    
#add_two_numbers_from_args(firstNumber, secondNumber)
#
#
##Mid-class challenge.
#def convert_distance(miles):
#    kilometers = (miles * 8.0) / 5.0
#    return "Converting distance in miles to kilometers:\nDistance in miles: " + str(miles) + ";\nDistance in kilometers: " + str(kilometers) + "." 
#
#print(convert_distance(44))
#print(convert_distance(122.5))
#
#def convert_distance_again(miles):
#    kilometers = (miles * 8.0) / 5.0
#    return "is " + str(miles) + "m, or " + str(kilometers) + "km."
#
#Ipswich_to_London = convert_distance_again(10)
#
#def distanceIpswichToLondon():
#    return "The distance from Ipswich to London {}".format(Ipswich_to_London)
#
#print(distanceIpswichToLondon())
#
##Task 4
#def convert_temperature(centigrade):
#    fahrenheit = centigrade * 9.0 / 5.0 + 32
#    kelvin = centigrade + 273.15
#    return "That's " + str(fahrenheit) + " in fahrenheit and " + str(kelvin) + " in kelvin."
#    
#print(convert_temperature(27))
#print(convert_temperature(-3))
#
#def temp_question():
#    print("What temperature is it in centigrade?")
#    tempOutside = int(input())
#    return convert_temperature(tempOutside)
#
#print(temp_question())
#
#def ageRelativeToHRH():
#    print("How old are you?")
#    currentAge = int(input())
#    if currentAge == 92:
#        years = "You are the same age as the Queen!"
#    elif currentAge > 92:
#        years = "You are " + str(currentAge - 92) + " years older than the Queen."
#    else:
#        years = "You are " + str(92 - currentAge) + " years younger than the Queen."
#    return years
#
#print(ageRelativeToHRH())
#
