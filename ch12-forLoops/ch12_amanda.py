# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:47:04 2018

@author: 612436198
"""

#Task 1: Loop through a list using for loop
my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]
for item in my_shopping_cart:
    print(item)
    
#Task 2: Update list values
values = [875, 23, 451]
for val in values:
    print("---> " + str(val))
    
for val in values:
    print("---> " + str(val + 50))
    
#Task 3: Create your own list
values = ["this", 55, "that"]
for item in values:
    print("***", item)
    
#Task 4: Loop through a string type
for char in "Yes":
    print(char)

for item in "co ding".split():
    print(item)
    
#Task 5: Loop through a tuple
code = (111, 222, 333)
for item in code:
    print(item)

#Task 6: Looping through a dictionary
salaryDict = {"al":20000, "bo":50000, "ced":1500}
for salary in salaryDict:
    print(salary) #prints keys
for salary in salaryDict:
    print(salaryDict[salary]) #prints values
salaryPairs = salaryDict.items()
for salary in salaryPairs:
    print(salary) #prints key value pairs

#Task 7: Looping through a sorted dictionary and selecting specific bits
densities = {"iron":(7.8, 5, 1000), "gold":(19.3, 20, 2), "zinc":(7.13, 10, 50), "lead":(11.4, 40, 200)}
metals = list(densities.keys())
print(metals)

metals.sort(reverse=True, key=lambda m:densities[m]) #sorting dictionary by keys in reverse order
print(metals)

#returning key value pairs:
for metal in metals:
    print(metal+":"+str(densities[metal]))

for item in sorted(densities.items()):
    print(item)
#this second one is better because it's only calling on one list to produce the result whereas the first one is calling on two.
    
keyValue = sorted(densities.items(), key=lambda kv:kv[1][1], reverse=True) #Sorting by second item in each value.

for item in keyValue:
    print(item)

#printing just one of the items for the value tuple:    
for metal, metalValue in keyValue:
    print(metal, metalValue[1])
    
for metal, metalValue in keyValue:
    print("Metal is", metal, "price is", metalValue[1])
    
for k, v in sorted(densities.items(), key=lambda kv:kv[1][1], reverse=True):
    print(k, v[1])
#again, this last one is better.

#for metal in metals:
#    print("{0:>8} = {1:5.1f}".format(metal, densities[metal])) #Google what the heck is going on here. (The f stands for float, you know that much. And it's something to do with the appearance maybe?)

#Task 8: Combine for loop and conditionals to filter out values    
for metal in densities:
    if densities[metal][0] > 8:
        print(metal)

for metal in densities:
    if str(densities[metal][0])[1] == ".":
        print(metal)

#Task 9: Design a sum function
values = [3, 12, 9]
total = 0
for val in values:
    print("Before adding", val, "total is", total)
    total += val #means same as total = total + val
    print("After adding", val, "total is", total)
print("TOTAL:" + str(total))

def sumValues(l):
    sumV = 0
    for val in l:
        sumV += val
    return sumV
print(sumValues(values))

#Task 10: Using a loop with index values
values = [3, 12, 9]

for i in range(len(values)):
    print(i)
#this gives 0, 1, 2 because values is three items long and range starts at zero - you're printing off each index position of the range of the list values

for i in range(len(values)):
    values[i] = values[i] ** 2
print(values)

for i in range(3, 10, 2): #start index, finish index, step
    print(i)
   
#Task 11: Using a loop with the range function
values = [3, 12, 9, 5, 6]
for index in range(1, len(values), 2):
    print(values[index], "with index", index)
    values[index] = values[index] ** 2
print(values)

#Task 12: Using break in for loops
nums = [1, 5, 30, 200, 101, 100, 22]
for n in nums:
    if n > 100:
        print("break:", n)
        break

for index in range(len(nums)):
    if nums[index] > 100:
        print("break:", nums[index], "with index", index)
        break
    
for index in range(len(nums)):
    print("loop index", index, "with value", nums[index])
    if nums[index] > 100:
        print("break:", nums[index], "with index", index)
        break
#Prints off everything until your break point. Can be useful with debugging.
        
#Counter
colours = ["red", "green", "red", "green", "blue", "green", "green"]
d = {}
for item in colours:
    if item not in d:
        d[item] = 1
        print(d, "first", item)
    else:
        d[item] += 1
    print(d)
    
#Task 13: Using nested loops
outer_vals_list = [1, 2, 3]
inner_vals_list = ["A", "B", "C"]
dict = {}
for outer_val in outer_vals_list:
    for inner_val in inner_vals_list:
        print(outer_val, inner_val)
        dict[outer_val] = inner_val
        if outer_val in dict:
            break
for outer_val in range(1, len(outer_vals_list)):
    for inner_val in range(1, len(inner_vals_list)):
        print(outer_vals_list[outer_val], inner_vals_list[inner_val])
        dict[outer_vals_list[outer_val]] = inner_vals_list[inner_val]
        if outer_vals_list[outer_val] in dict:
            break
for outer_val in range(2, len(outer_vals_list)):
    for inner_val in range(2, len(inner_vals_list)):
        print(outer_vals_list[outer_val], inner_vals_list[inner_val])
        dict[outer_vals_list[outer_val]] = inner_vals_list[inner_val]
print(dict)
#Come back to this as this can't be the right solution!

#Task 14: Multiplication table with a for loop
for i in range(1, 11):
    for j in range(1, 11):
        print("{0:>3}".format(i * j), end="")
    print("\n")