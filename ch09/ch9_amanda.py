# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:36:56 2018

@author: 612436198
"""
##LISTS
#my_favourite_fruits = ["apple", "orange", "banana"]
#
#x = ["this", 55, "that", my_favourite_fruits]
#
##prints the element at position 3 in the list:
#print(x[3])
#
##prints the element at position 1 of the element at position 3 in the list:
#print(x[3][1])
#
##prints the element at positition 2 of the element at position 1 of the element at position 3 in the list:
#print(x[3][1][2])
#
##you can use negative numbers too (the number it's counting back from is len(list) - so for a list with four elements, position -1 is position (4 - 1) ie position 3):
#print(x[-1])
#
##you can remove items from lists (this method only works for lists):
#x.remove(my_favourite_fruits)
#print(x)
#
##you can change items in lists (they are MUTABLE):
#x[1] = "and"
#print(x)
#
##you can append things to lists (this method only works for lists):
#x.append("again")
#print(x)
#
##be careful, because this will change x, but not create a new list y:
#y = x.append("hello")
#print(x)
#print(y)
#
##if you make y a clone of x anything you do to either will happen to the other:
#y = x
#x.remove("hello")
#print(x)
#print(y)
#y.append("ok")
#print(x)
#print(y)
#
##trying out the del function:
#del(x[4])
#print(x)
#
##trying out the pop method:
#x.pop()
#print(x)
#
##you can perform some (not all) mathematical operations on lists:
#x = ["the", "cat", "sat"]
#y = ["on", "the", "mat"]
#
#z = x * 2
#print(z)
#
#z = x + y
#print(z)
#
##trying out the set function (produces a dictionary):
#print(set(x+y))
#a = set(z)
#print(a)
##NB dictionaries are an unordered data type, so will print in whatever order makes sense to it at the time!
##the original lists haven't changed:
#print(x)
#print(y)
#print(z)
#
##slicing a list:
#x = ["this", "and", "that", "once", "again"]
#print(x[1:4])
##note this gives you up to but not including position 4. Before colon is inclusive, after colon is exclusive.
##if you leave one side of the colon empty it will default to the extreme (so 0 for before and len(list) for after):
#print(x[:3])
#print(x[1:])
##you can also use negatives:
#print(x[1:-2])
#print(x[-3:5])

##SORTING LISTS
#x = [7, 11, 3, 9, 2]
#
#y = sorted(x)
#print(y)
#
#x.sort()
#print(x)
#
#x = ["d", "j", "s", "o", "a"]
#print(x)
#x.sort()
#print(x)
##Generally speaking, if a function is one where you're putting an input in the brackets after it, it will take that input, change it and give you a new output (the original input is unaffected). If the function is one where you put the thing first then a dot then the function with brackets, it will change that input.
#
##reverse sort:
#x = [7, 11, 3, 9, 2]
#print(sorted(x))
#print(sorted(x, reverse=True))
#
#x.sort()
##you can't just print this, it will return none. Because that function does not give a return value (see comment starting 'Generally speaking...' above).
#print(x)
#
#x.sort(reverse=True)
#print(x)
#
#y = ["banana", "satsuma", "chocolate", "apple", "carrot"]
#print(sorted(y))
#print(sorted(y, reverse=True))
#
#y.sort()
#print(y)
#y.sort(reverse=True)
#print(y)
#
##TUPLES
#
##List example 1:
#a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#del(a[-1])
#print(a)
#
##Tuple example 1:
#b = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
##del b[-1]
##print(b)
##del function doesn't work on tuples! They are IMMUTABLE.
#
##List example 2:
#a[3] = 10
#print(a)
#
##Tuple example 2:
##b[3] = 10
##print(b)
#
##List example 3:
#a.append(3)
#print(a)
#
##Tuple example 3:
##b.append(3)
##print(b)
#
##Tuples and lists are both compound data types, which means they can contain elements of different types: [1, "two", 3.0] and (1, "two", 3.0) are both fine.
#
##You can switch between lists and tuples:
#a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#c = tuple(a)
#print(c)
#
#b = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#c = list(b)
#print(c)

#lambda stuff

#x = ["cs", "yw", "hd", "zs", "ab"]
#y = sorted(x)
#z = ["zs", "yw", "hd", "cs", "ab"]
#x2 = [("a", 3, z), ("c", 1, y), ("b", 5, x)]
#
#print(sorted(x2))
#print(sorted(x2, key=lambda s:s[1]))
#print(sorted(x2, key=lambda s:s[2]))
#print(sorted(x2, key=lambda s:s[2][1]))

a = [50, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
c = [2, 2, 3, 3, 4, 5, 6, 7, 8, 9]
myFavF = ["apple", "orange", "banana"]
x = ["lf", "sb", "hw", "aa", "ed", "fy"]
z = ["uj", "fg", "uj", "ww", "sx", "cf"]
y = sorted(x)
x2 = [(a, 3, "a", z), (c, 1, "c", y), (b, 5, "b", x)]

print(sorted(x2, key=lambda s:s[0][1]))
print(sorted(x2, key=lambda s:s[3][2][1]))

#you can select a position at the same time as sorting:
print(sorted(x2, key=lambda s:s[1])[0])
