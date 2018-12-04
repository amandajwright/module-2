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
##LPtHW Ex18
#def print_two(*args):
#    arg1, arg2 = args
#    print("arg1: {}, arg2: {}".format(arg1, arg2))
#    
#def print_two_again(arg1, arg2):
#    print("arg1: {}, arg2: {}".format(arg1, arg2))
#    
#def print_one(arg1):
#    print("arg1: {}".format(arg1))
#    
#def print_none():
#    print("I got nothin'.")
#    
#print_two("Zed", "Shaw")
#print_two_again("Zed", "Shaw")
#print_one("First!")
#print_none()
#
##LPtHW Ex19
#def cheese_and_crackers(cheese_count, boxes_of_crackers):
#    print("You have {} cheeses!".format(cheese_count))
#    print("You have {} boxes of crackers!".format(boxes_of_crackers))
#    print("Man that's enought for a party!")
#    print("Get a blanket.\n")
#    
#print("We can just give the function numbers directly:")
#cheese_and_crackers(20, 30)
#
#print("OR, we can use variables from our script:")
#amount_of_cheese = 10
#amount_of_crackers = 50
#
#cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#
#print("We can even do math inside too:")
#cheese_and_crackers(10 + 20, 5 + 6)
#
#print("And we can combine the two, variables and math:")
#cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#
##LPtHW Ex19 Study Drill 3.
#def christmasPresents(people, presents):
#    print("There are {} people in my family.".format(people))
#    print("They expect to receive {} presents each.".format(presents))
#    print("Better get shopping!")
#
#print("The first way:")    
#christmasPresents(4, 3)
#
#print("The second way:")
#people = 2
#presents = 5
#christmasPresents(people, presents)
#
#print("The third way:")
#christmasPresents(3 + 4, 2)
#
#print("The fourth way:")
#christmasPresents(people + 1, presents - 2)
#
#print("The fifth way:")
#def peopleInFamily():
#    parents = 2
#    brothers = 2
#    sisters_law = 2
#    nieces_nephews = 3
#    aunts_uncles = 3
#    cousins = 2
#    grandparents = 1
#    return parents + brothers + sisters_law + nieces_nephews + aunts_uncles + cousins + grandparents
#def presentsExpectedByEach():
#    return 2
#
#christmasPresents(peopleInFamily(), presentsExpectedByEach())
#
#print("The sixth way:")
#peopleInFamily = peopleInFamily()
#presentsExpectedByEach = presentsExpectedByEach()
#christmasPresents(peopleInFamily, presentsExpectedByEach)
#
#print("The seventh way:")
#christmasPresents(peopleInFamily, 3)
#
#print("The eighth way:")
#christmasPresents(10, presentsExpectedByEach)
#
#print("The ninth way:")
#def christmasPresentsSpecific():
#    christmasPresents(15,2)
#christmasPresentsSpecific()
#
#print("The tenth way:")
#def christmasPresentsSpecificAgain():
#    people = 7
#    presents = 3
#    return christmasPresents(people, presents)
#christmasPresentsSpecificAgain()
#
##LPtHW Ex20 asks to import from sys, so have skipped this one.

#LPtHW Ex21

def add(a, b):
    print("ADDING {} + {}".format(a, b))
    return a + b

def subtract(a, b):
    print("SUBTRACTING {} - {}".format(a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING {} * {}".format(a, b))
    return a * b

def divide(a, b):
    print("DIVIDING {} / {}".format(a, b))
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: {}, Height: {}, Weight: {}, IQ: {}".format(age, height, weight, iq))

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "Can you do it by hand?")

#LPtHW Ex21 Study Drill 2:
#what = 35 + (74 - ((180 * (50 / 2))))

#LPtHW Ex21 Study Drill 4:
#formula = 24 + 34 / 100 - 1023
formula = subtract(divide(add(24, 34), 100), 1023)
print(formula)