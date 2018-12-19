# -*- coding: utf-8 -*-


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

##Task 3: Using conditional statements

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
##Or - in fact preferably: (Task 4: Using else statements)
#
#if number > 10:
#    print("Too high!")
#
#elif number <= 0:
#    print("Too low!")
#    
#else:
#    print("Thank you!")

##Task 5: Using elif statements

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
##NB the order of your if and elif statements is important - put the narrowest class first.   
