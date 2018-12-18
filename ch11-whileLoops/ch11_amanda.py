# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:09:19 2018

@author: 612436198
"""

#x = 33
#while x >= 1:
#    print(x, ":", end=" ")
#    x = x / 2
#print(x) #exiting the while loop, when the condition is no longer True
#
##The 'end' above defines what separates what you're printing from the next thing that's going to print (the default is to print on a new line, the above says not on a new line, just after a space).
#
##pseudo-code for triangular number example:
##first you have a number, n
##you need to establish if n is greater than 0
##if it is, minus one from it and add it to itself, so n + (n - 1)
##reassign n - 1 as the new n
##add the new n to the result of the previous sum each time
##stop when n reaches zero
#
#def triangular(n):
#    trinum = 0
#    while n > 0:
#        trinum = trinum + n
#        n = n - 1
#    return trinum
#
##second example
#mark = 1
#while mark > 0:
#    mark = int(input("What mark did you get? "))
#    if mark >= 70:
#        print("First class.")
#    elif mark >= 40:
#        print("Pass.")
#    else:
#        print("Fail.")

##to get out of second example:
#didYouPass = 'Yes'
#
#while didYouPass == 'Yes':
#   mark = int(input('What is your score? '))
#   if mark >= 70 and mark <=90:
#       print('FIRST CLASS')
#   elif mark >= 40:
#       print('PASS')
#   elif mark < 40:
#       print('FAIL')
#   didYouPass = input('Did you pass? ')
       
##Using break:
#i = 55
#while i > 10:
#    print(i)
#    i = 1 * 0.8
#    if i == 35.2:
#        break
#A 'break' statement in a loop immediately terminates the current iteration and ends the loop overall. This can be very useful, for example when you just want to test part of a loop to evaluate results.
        
#Second break example
name = ""
while type(name) == str:
    name = input("Enter name: ").title()
    if name == "Done":
        break
    else:
        print("Hello {}!".format(name))

