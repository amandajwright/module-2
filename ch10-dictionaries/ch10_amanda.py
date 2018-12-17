# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:55:38 2018

@author: 612436198
"""

#DICTIONARIES

#myFirstDictionary = {"bo":50000, "al":20000, 7:("Joke", "Chen", "Bond")}
#print(myFirstDictionary)
##NB numbers cannot begin with zero if being assigned to keys in a dictionary.
#
##You can create an empty dictionary:
#
#salary = {}
#print(salary)
#
##then assign values to new keys:
#salary["al"] = 20000
#print(salary)
#
#salary["bo"] = 50000
#print(salary)
#
#salary["cr"] = 80000
#print(salary)
#
##and assign new values to existing keys:
#salary["al"] = 20500
#print(salary)
#
##or do mathematical operations with existing keys' values:
#salary["al"] += 2000
#print(salary)

##You can create dictionaries with keys and values already included:
#tel = {"amanda":858, "loren":264, "mabel":914, "ottilie":344}
#print(tel)
#
#tel["amanda"] = 5858
#tel["loren"] = 8264
#tel["mabel"] = 3914
#tel["ottilie"] = 8344
#print(tel)
#
#tel["harriet"] = 989
#print(tel)
#
##Deleting an item from a dictionary (have to delete both the key and the value, they go everywhere together):
#del tel["harriet"]
#print(tel)
#
##If you use variables as keys, the real value of the variable will appear in the dictionary as the key:
#one = 1
#two = 2
#three = 3
#variablesAsKeys = {one:123, two:234, three:345}
#print(variablesAsKeys)
#
##Getting all the keys or all the values from a dictionary (these methods only work on dictionaries):
#print(tel.keys())
#print(tel.values())
#
##You might want to have lists of keys or values (because you can do more with lists):
#keysOfTel = list(tel.keys())
#print(keysOfTel)
#valuesOfTel = list(tel.values())
#print(valuesOfTel)
##for example, now you can retrieve individual keys by position if you want to:
#print(list(tel.keys())[0])
##Getting the value for a key:
#print(tel["loren"])
##Finding out if a key is in a dictionary:
#if "eric" in tel:
#    print("eric:", tel["eric"])
#else:
#    print("'eric' not found")
##or (this makes it easier to change to search for different keys):
#k = "mabel"
#if k in tel:
#    print(k, ":", tel[k])
#else:
#    print(k, "not found")

##Sorting dictionaries.
#counts = {"a":3, "c":1, "b":5}
##Make a list of keys:
#labels = list(counts.keys())
##Sorting by value:
#labels.sort(key=lambda k:counts[k])  #because remember counts[k] returns the value of k
#print(labels)
#
##Practice:
#studentInfo = {"amanda":["november", 9], "mabel":["april",8], "loren":["august",1], "ottilie":["may",3]}
#student_key = list(studentInfo.keys())
#student_key.sort(key=lambda k:studentInfo[k])
#print(student_key)
##Sorting by second bit of info in list associated with a key:
#student_key.sort(key=lambda k:studentInfo[k][1])
#print(student_key)
##Adding info to keys:
#studentInfo["amanda"].append("green")
#print(studentInfo)
#
#print(sorted(student_key))
#print(sorted(student_key, key=lambda k:studentInfo[k]))
#
##To get both key and value (the key+value pairs are returned as tuples):
#print(sorted(studentInfo.items(), key=lambda kv:kv[1]))
#
##Reverse order:
#student_key.sort(key=lambda k:studentInfo[k], reverse=True)
#print(student_key)
#
#student_key.sort(key=lambda k:studentInfo[k][1], reverse=True)
#print(student_key)
#
#print(sorted(student_key, key=lambda k:studentInfo[k], reverse=True))
#print(sorted(student_key, key=lambda k:studentInfo[k][1], reverse=True))
#
#print(sorted(studentInfo.items(), key=lambda kv:kv[1], reverse=True))

#Task from book.
metals = {"iron":[7.8, 2.3, 13.7], "gold":[19.3, 4.5, 2.3], "zinc":[7.13, 3.5, 56.9], "lead":[11.4, 1.2, 42.7]}

metals_k = list(metals.keys())

metals_k.sort(key=lambda k:metals[k][1], reverse=True)
print(metals_k)

print(sorted(metals.items(), key=lambda kv:kv[1][1], reverse=True))