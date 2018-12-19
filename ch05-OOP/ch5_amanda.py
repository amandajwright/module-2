# -*- coding: utf-8 -*-


##Task 1: Using classes
#class Customer(object):
#    
#    def __init__(self, name, balance=0.0):
#        self.name = name
#        self.balance = balance
#    
#    def withdraw(self, amount):
#        if amount > self.balance:
#            raise RuntimeError("Amount greater than available balance.")
#        self.balance -= amount
#        return self.balance
#    
#    def deposit(self, amount):
#        self.balance += amount
#        return self.balance
#    
#jason = Customer("Jason Taylor", 1000.0)
#bob = Customer("Bob Jones", 325.5)
#agnes = Customer("Agnes Denton", 2439.0)

##Inheritance animal example
#
#class Animal():
#    def eat(self):
#        print("yum")
#class Dog(Animal):
#    def bark(self):
#        print("Woof!")
#class Cat(Animal):
#    def meow(self):
#        print("Meow")
#        
#rufus = Dog()
#rufus.bark()
#rufus.eat()
#
#monkey = Animal()
#monkey.eat()
#
#Task 2: Using inheritance (robot example)
#
#class Robot():
#    def move(self):
#        print("... move move move ...")
#class CleanRobot(Robot):
#    def clean(self):
#        print("I vacuum dust")
#class CookRobot(Robot):
#    def cook(self):
#        print("I make rice.")
#
#bertha = CleanRobot()
#bertha.move()
#bertha.clean()
#
##Task 3: Using inheritance
#johnnyFive = CookRobot()
#johnnyFive.cook()

##More levels of inheritance (inheritance practice):
#
#class Food():
#    def action(self):
#        print("Eat.")
#
#class Fruit(Food):
#    def reason(self):
#        print("Good for you.")
#
#class Apple(Fruit):
#    def taste(self):
#        print("Nice.")
#
#class Banana(Fruit):
#    def colour(self):
#        print("Yellow.")
#
#class Veg(Food):
#    def disposition(self):
#        print("Dislike.")
#
#class Cabbage(Veg):
#    def ranking(self):
#        print("The worst.")
#
#pinkLady = Apple()
#pinkLady.action()
#pinkLady.reason()
#pinkLady.taste()
#
#cauliflower = Veg()
#cauliflower.action()
#cauliflower.disposition()

#Christmas presents example

#class FamilyMember():
#    def __init__(self, name, budget=0):
#        self.name = name
#        self.budget = budget
#    def isPresentRequired(self):
#        presentBought = input("Have you bought {} a present yet? (Type y for yes, n for no.) ".format(self.name))
#        if presentBought == "y":
#            budgetSpent = input("How much did you spend on it? £")
#            self.budget = self.budget - int(budgetSpent)
#            if self.budget > 0:
#                return "You have £{} left to spend on {}.".format(self.budget, self.name)
#            elif self.budget == 0 and (self.name == "the Elleringtons" or self.name == "Grandma, Jan and Chris"):
#                return "{} are sorted!".format(self.name)
#            elif self.budget == 0:
#                return "{} is sorted!".format(self.name)
#            else:
#                return "Whoops! You spent too much."
#        else:
#            return "Get on with it!"
#        
#class Parent(FamilyMember):
#    def inspiration(self):
#        tickets = input("Are there any concerts or shows they might be interested in?  (Type y for yes, n for no.) ")
#        if tickets == "y":
#           return "Get them tickets to that."
#        else:
#           lastYearsPresent = input("What did you get them last year? ")
#           sameAgain = input("Can you get them {} again? (Type y for yes, n for no.) ".format(lastYearsPresent))
#           if sameAgain == "y":
#               return "So do that!"
#           else:
#               return "Aaargh!"
#        
#class Brother(FamilyMember):
#    def makeLifeEasier(self):
#        jointPresent = input("Can you piggyback on anyone else's present? (Type y for yes, n for no.) ")
#        if jointPresent == "y":
#            return "So do that!"
#        else:
#            return "Aaargh!"
#        
#class SisterInLaw(FamilyMember):
#    def thinkOfSomething(self):
#        print("Not a clue.")
#        print("Aaargh!")
#        
#class Niece_Nephew(FamilyMember):
#   def __init__(self, name, budget=0):
#       self.name = name
#       self.budget = budget
#   def ideasForPresents(self):
#       if self.name == "Charlton":
#           ideasList = input("Has he written a letter to Father Christmas? (Type y for yes, n for no.) ")
#           if ideasList == "y":
#               ideasWithinBudget = input("Did he ask for anything that costs {} or less? (Type y for yes, n for no.) ".format(self.budget))
#               if ideasWithinBudget == "y":
#                   return "Buy {} something he asked Father Christmas for.".format(self.name)
#               else:
#                   return "Find a cheaper version of whatever {} asked Father Christmas for.".format(self.name)
#       elif self.name == "Tallulah" or self.name == "Lucy":
#           ideasList = input("Has she written a letter to Father Christmas? (Type y for yes, n for no.) ")
#           if ideasList == "y":
#               ideasWithinBudget = input("Did she ask for anything that costs {} or less? (Type y for yes, n for no.) ".format(self.budget))
#               if ideasWithinBudget == "y":
#                   return "Buy {} something she asked Father Christmas for.".format(self.name)
#               else:
#                   return "Find a cheaper version of whatever {} asked Father Christmas for.".format(self.name)
#       else:
#            return "Aaargh!"
#        
#class ExtendedFamily(FamilyMember):
#    def noOfPresentsRequired(self):
#        togetherAtChristmas = input("Are they going to be together for Christmas this year? (Type y for yes, n for no.) ")
#        if togetherAtChristmas == "y":
#            return "Just one order required."
#        else:
#            return "Two orders required."
#        
#mum = Parent("Mum", 100.0)
#dad = Parent("Dad", 100.0)
#sam = Brother("Sam", 90.0)
#oscar = Brother("Oscar", 90.0)
#rochelle = SisterInLaw("Rochelle", 80.0)
#karen = SisterInLaw("Karen", 80.0)
#tallulah = Niece_Nephew("Tallulah", 70.0)
#charlton = Niece_Nephew("Charlton", 70.0)
#lucy = Niece_Nephew("Lucy", 70.0)
#mums_side = ExtendedFamily("the Elleringtons", 60.0)
#dads_side = ExtendedFamily("Grandma, Jan and Chris", 60.0)

##Task 4: Using association

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print("yum")
        
class Dog(Animal):
    def bark(self):
        print("Woof!")

class Robot():
    def move(self):
        print("... move move move ...")
class CleanRobot(Robot):
    def clean(self):
        print("I vacuum dust")

class SuperRobot():
    def __init__(self, name, age):
        #This class contains 3 objects.
        self.name = name
        self.age = age
        
        self.o1 = Robot()
        self.o2 = Dog(name, age)
        self.o3 = CleanRobot()
    def playGame(self):
        print("alphago game")
    def move(self):
        return self.o1.move() #using robot class method
    def bark(self):
        return self.o2.bark() #using dog class method
    def clean(self):
        return self.o3.clean() #using cleanrobot class method

name = input("pet's name: ")
age = int(input("pet's age: "))
    
machineDog = SuperRobot(name, age)
machineDog.move()
machineDog.bark()