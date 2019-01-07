# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:06:43 2019

@author: 612436198
"""

#Task 1: Initialising with parameters

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        if gender == "m":
            self.isMale = True
        elif gender == "f":
            self.isMale = False
        else:
            print("Gender not recognised!")

#Task 2: Defining functions/methods for a class           
    def greetingInformal(self):
        print("Hi", self.name)
              
    def greetingFormal(self):
        if self.isMale:
            print("Welcome, Mr", self.name)
        else:
            print("Welcome, Ms", self.name)

#Task 3: Adding a greeting filter, a method that calls another method
    def greetingAgeBased(self):
        if self.age < 18:
            print("Welcome, young", self.name)
        elif self.age > 60:
            print("Welcome, venerable", self.name)
        else:
            self.greetingFormal()

#Task 4: Creating a subclass
class Wizard(Person):
    #Task 5: Using a new __init__ method definition for the subclass
    def __init__(self, name, age, gender):
        Person.__init__(self, name, age, "m")

    #Changing a method that exists in superclass
    def greetingFormal(self):
        print("Welcome, Mr", self.name, end="")
        print("- you're a fine wizard!")
        
    #Creating new method for subclass
    def spell(self):
        print("Expelliarmus!")

p1 = Person("Harry", 12, "m")
p2 = Person("Hermione", 11, "f")
p3 = Person("Dumbledore", 107, "m")
p4 = Person("JK", 58, "f")
p5 = Wizard("Ron", 12, "m")
print("Task 1:")
print(p1.name)
print(p1.isMale)
print("Task 2:")
print(p1.greetingInformal())
print(p1.greetingFormal())
print(p2.greetingFormal())
print("Task 3:")
print(p2.greetingAgeBased())
print(p3.greetingAgeBased())
print(p4.greetingAgeBased())
print("Task 4:")
print(p5.greetingFormal())
print("Task 6:")
print(p5.spell())