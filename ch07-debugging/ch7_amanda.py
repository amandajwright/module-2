# -*- coding: utf-8 -*-



#Using print function
#Task 1
userInput = input("please give a number")
result = userInput - 2
print(result)
#this gives an error, because the user input is a string rather than an input:
userInput = input("please give a number")
print(type(userInput))

#to resolve this:
userInput = int(input("please give a number"))
result = userInput - 2
print(result)

#Using breakpoints
#Task 2
userInput = input("please give a number")
def simpleOperation(userInput):
    intInput = int(userInput)
    result = intInput - 2
    return result
def nestedOperation(result):
    result = simpleOperation(userInput)
    result2 = result * 2
    return result2
result =simpleOperation(userInput)
result2 = nestedOperation(result)
print(result2)

"""
When you've used a breakpoint you don't run the code in the normal way with the green arrow, you use the blue buttons:
    1st: start running your code until the breakpoint
    2nd: allows you to run your code line by line until the breakpoint
    3rd: for stepping into the sections (class and functions) that you would like to dig into more and...
    ...4th: for you to step out when you feel that the error is not realted to the current section
    5th: to go to the next breakpoint (if you have set up multiple ones)
    6th: for you to exit debugging mode and go back to normal coding mode
To create a breakpoint in Spyder, double click to the left of the line number.
"""