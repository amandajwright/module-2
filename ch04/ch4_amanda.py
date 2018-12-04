# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:47:08 2018

@author: 612436198
"""

##Generating a random number from a given range and timing how long a function takes to run.
#
#import random
#import datetime
#import time
#
#def luckyNumberRandom():
#    name = input("Please type your name: ")
#    print("Hello " + name.upper())
#    number = int(input("Please type a number: "))
#    
#    print("Your lucky number is: " + str(random.randint(50,number)))
#
#startTime = time.time()
#
#luckyNumberRandom()
#
#print("Date and time", datetime.datetime.now())
#print()
#print("Current time", datetime.datetime.now().time())
#
#processTime = time.time()-startTime
#
#print()
#print("Program running time: ", round(processTime,2), "seconds")

#Task 3

#number = input("Enter a number between 1 and 10: ")
#number = int(number) #Converts the input string to an integer.

#if number > 10:
#    print("Too high!")
#    
#if number <= 0:
#    print("Too low!")
#    
#if 1 <= number <= 10:
#    print("Thank you!")
#    
#Or - in fact preferably:

#if number > 10:
#    print("Too high!")
#
#elif number <= 0:
#    print("Too low!")
#    
#else:
#    print("Thank you!")

#Task 5.

#age = input("How old are you? ")
#age = int(age) #Converts the input string to an integer.
#
#if age < 13:
#    print("child")
#
#elif age < 18:
#    print("teen")
#
#elif age < 65:
#    print("adult")
#
#else:
#    print("pensioner")
    
#LPtHW Ex11

#print("How old are you?"),
#age = input()
#print("How tall are you?"),
#height = input()
#print("How much do you weigh?"),
#weight = input()
#
#print("So, you're {} old, {} tall and {} heavy.".format(age, height, weight))

#LPtHW Ex12
#
#age = input("How old are you? ")
#height = input("How tall are you? ")
#weight = input("How much do you weigh? ")
#
#print("So, you're {} old, {} tall and {} heavy.".format(age, height, weight))

##LPtHW Ex29
#
#people = 20
#cats = 30
#dogs = 15
#
#if people < cats:
#    print("Too many cats! The world is doomed!")
#
#if people > cats:
#    print("Not many cats! The world is saved!")
#
#if people < dogs:
#    print("The world is drooled on!")
#
#if people > dogs:
#    print("The world is dry!")
#
#
#dogs += 5
##The code x += 1 is the same as doing x = x + 1 but involves less typing. You can call this the “increment by” operator. The same goes for - = and many other expressions you’ll learn later.
#
#if people >= dogs:
#    print("People are greater than or equal to dogs.")
#
#if people <= dogs:
#    print("People are less than or equal to dogs.")
#
#if people == dogs:
#    print("People are dogs.")

#LPtHW Ex30
#
#people = 30
#cars = 40
#buses = 15
#
#if cars > people:
#    print("We should take the cars.")
#elif cars < people:
#    print("We should not take the cars.")
#else:
#    print("We can't decide.")
#    
#if buses > cars:
#    print("That's too many buses.")
#elif buses < cars:
#    print("Maybe we could take the buses.")
#else:
#    print("We still can't decide.")
#
#if people> buses:
#    print("Alright, let's just take the buses.")
#else:
#    print("Fine, let's stay home then.")

#LPtHW Ex31

print("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    
    bear = input("< ")
    
    if bear == "1":
        print("The bear eats your face off. good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing {} is probably better. Bear runs away.".format(bear))
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. good job!")
    else:
        print("The insanity rots your eyes into  apool of muck. Good job!")

else:
    print("You stumble around and fall on a knife and die. good job!")
    