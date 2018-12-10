# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 12:07:55 2018

@author: amand
"""

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