#!/usr/bin/env/ python3

myString = ('sapiens, erectus, neanderthalensis')

print(myString)

myList = myString.split(',')

#print(myList, 'is a', type(myList))
print(sorted(myList,key = len))

print("\nDone.\n")
