# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:55:59 2018

@author: 612436198
"""
#Different ways of having a person answer a question and using the answer.
#Also the different ways of applying the title function to the answer.
print("What's your name?")
name = input()
print("Hello {}!".format(name.title()))

print("What's your last name?")
name = input().title()
print("Hey {}.".format(name))

name = input("What's your name? ")
name = name.title()
print("Hello {}!".format(name))

#Just asking someone a question and storing their answer as a variable.
age = input("Please type your age: ")

#Using input and format functions together.
print("What's your first name?")
firstName = input().title()
print("What's your last name?")
lastName = input().title()
print("Hello {} {}!".format(firstName,lastName))

#Using input and format functions together retrieving more than one piece of info from one answer.
print("Please type your name and where you're from separated by a comma.")
namePlace = input()
namePlaceList = namePlace.split(",")
print("Hello {} from {}.".format(namePlaceList[0], namePlaceList[1]))

#Writing your first function.
def hello_world():
    print("Hello World!")

#Calling your first function.    
hello_world()

#Task2 from lecture slides.
#Task2(1), (2)
def myName():
    print("Amanda")
    print(2+2)

myName()

#Task2(3)    
def secondMyName():
    print("What's your name?")
    myName = input()
    print(myName)
    
secondMyName()

#Task2 Challenge
def secondHelloWorld():
    print("Hello World!")
    secondMyName()

secondHelloWorld()

#Task2_2
def hello_world_2args(a, b):
    print("{} {}".format(a,b))
    
a1 = "hello"
b1 = "world"
a2 = "love"
b2 = "coding"

hello_world_2args(a1, b1)

hello_world_2args(a2, b2)

def hello_world_4args(a, b, c, d):
    print("{} {} i {} {}".format(a,b,c,d))

hello_world_4args(a1, b1, a2, b2)

#Adding two inputted numbers
def add_two_input_nos():
    print("Please type a number:")
    firstNumberTyped = input()
    print("Please type another number:")
    secondNumberTyped = input()
    print(int(firstNumberTyped) + int(secondNumberTyped))
    
add_two_input_nos()

#Functions with different numbers of arguments.
print(range(10))
print(range(1,10))
print(range(1,10,2))

#Task 3
def add_two_numbers():
    adding = 3 + 4
    print(adding)
    
add_two_numbers()

def add_two_numbers_from_args(a, b):
    print(a + b)

firstNumber = 1
secondNumber = 2
    
add_two_numbers_from_args(firstNumber, secondNumber)
