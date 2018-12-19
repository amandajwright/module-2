# -*- coding: utf-8 -*-


from ch3file1_amanda_function import *

#The star means "everything".

print(presentsExpectedByEach())
print(ageRelativeToHRH())

#If do as import MyFirstLibrary, need to put that in front of functions:

#print(MyFirstLibrary.presentsExpectedByEach())
#print(MyFirstLibrary.ageRelativetoHRH())


#Can also import specific functions from a library:

#from MyFirstLibrary import ageRelativeToHRH
#print(ageRelativeToHRH())


#Task 1: Input from a user
print("what is your name?")
name = input()
print("Hello {}!".format(name))

#Task 2 (Write your first function) test:
myName()

#Task 4 (Adding two numbers together) test:
add_two_numbers_from_args(5, 10)
add_two_numbers_from_args(1, 137)

#Task 5 (Temperature conversion) test:
def temp_question():
    
#Task 6 (Return value) test:
returned_value = add_two_numbers_and_return_value()
print(returned_value)
print(returned_value - 5)