# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print (5 - 6)
print (8 * 9)
print (6 / 2)
print (5 / 2)
print (5.0 / 2)
print (5 % 2)
print (2 * (10 + 3))
print (2 ** 4)
age = 5
age = "almost three"
age = 29.5
age = "I really don't know!"
print(age)
print("hello" + "world")
print("Joke" * 3)
print("Chen" + "3")
print("hello".upper())
print("GOODBYE".lower())
print("the lord of the rings".title())
age = "I don't know."
printAge = type(age)
print(printAge)
S1 = "hello " + "world"
S2 = "Joke" * 3
S3 = 5
print(S1 + S2 * 10)
print(S1 + S2 + str(S3))
strExample = "a,b,b,d,happy"
print(strExample.split(","))
age = 5
like = "painting"
age_description = "My age is {} and I like {}.".format(age,like)
print(age_description)
age_description_two = "My age is {0} and I like {1}.".format(age,like)
print(age_description_two)
age_description_three = "My age is {0} and I like {1}. My brother also likes {1}.".format(age,like)
print(age_description_three)
age_description_four = "My age is {0} and I like {1}. My brother is also {0} and also likes {1}.".format(age,like)
print(age_description_four)
testingQuotes = """does this work?"""
print(testingQuotes)
"""
this should be ignored?
"""
test_return = """Can you add
returns if you use
three quotes?"""
print(test_return)

#homework

print(10 / 3)
print(10 % 3)
a = 1
a = a + 1
print(a)
b = "hello"
print(b)
c = b.title()
print(b)
print(c)
d = "hello"
e = d.title()
print(d)
print(e)
name = "Dave"
f = "Hello {0}!".format(name)
print(f)
name = "Sarah"
print(f)
print(f * 5)

#LPtHW ex1

print("Hello World!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print("Yay! Printing.")
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

#LPtHW ex2

#A comment, this is so you can read your program later.
#Anything after the # is ignored by python.
print("I could have code like this.") # and the comment after is ignored
#you can also use a comment to "disable" or comment out a piece of code:
#print "This won't run."
print("This will run.")

#LPtHW ex3

#Prints the str.
print("I will now count my chickens:")

#Prints the str followed by the float result of the sum (which is a float).
print("Hens", 25 + 30 / 6)

#Prints the str followed by the result of the sum (which is an int).
print("Roosters", 100 - 25 * 3 % 4)

#Prints the str.
print("Now I will count the eggs:")

#Prints the result of the sum (which is a float).
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

#Prints the str.
print("Is it true that 3 + 2 < 5 - 7?")

#Prints whether the statement in the brackets is True or False.
print(3 + 2 < 5 - 7)

#Prints the str followed by the result of the sum (an int).
print("What is 3 + 2?", 3 + 2)

#Prints the str followed by the result of the sum (a negative value int).
print("What is 5 - 7?", 5 - 7)

#Prints the str.
print("Oh, that's why it's False.")

#Prints the str.
print("How about some more.")

#Prints the str followed by whether the statement is True or False.
print("Is it greater?", 5 > -2)

#Prints the str followed by whether the statement is True or False.
print("Is it greater or equal?", 5 >= -2)

#Prints the str followed by whether the statement is True or False.
print("Is it less or equal?", 5 <= -2)

#LPtHW Ex4

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#On line 8 in the python editor, you were trying to give a variable a value using a variable that hadn't been defined.

#LPtHW Ex5

name = "Zed A. Shaw"
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = "Blue"
teeth = "White"
hair = "Brown"

print("Let's talk about {}.".format(name))
print("He's {} inches tall.".format(str(height)))
print("He's {} pounds heavy.".format(str(weight)))
print("Actually that's not too heavy.")
print("He's got {} eyes and {} hair.".format(eyes,hair))
print("His teeth are usually {} depending on the coffee.".format(teeth))

# this line is tricky, try to get it exactly right
print("If I add {}, {} and {} I get {}.".format(str(age),str(height),str(weight),str((age + height + weight))))

height_in_cm = height * 2.54 # 1 inch equals 2.54 cm.
weight_in_kg = weight * 0.45 # 1 lb equals 0.45 kg.

#LptHW Ex6
x = "There are {} types of people.".format(str(10))
binary = "binary"
do_not = "don't"
y = "Those who know {} and those who {}.".format(binary,do_not)

print(x)
print(y)

print("I said: {}.".format(x))
print("I also said: '{}'.".format(y))

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

#LPtHW Ex7

print("Mary had a little lamb.")
print("Its fleece was white as {}.".format("snow"))
print("And everywhere that Mary went.")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6)
print(end7 + end8 + end9 + end10 + end11 + end12)

#LPtHW Ex8

#? Can this be done in Python 3 ?

#LPtHW Ex9

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

#LPtHW Ex10

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

"""
Finish Learn Python the Hard Way exercises 1 to 10.
"""