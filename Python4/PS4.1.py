#!/usr/bin/env python3

import sys

myString = 'sapiens, erectus, neanderthalensis'

print(myString)

myList = myString.split(', ')

print(sorted(myList))

print(sorted(myList, key = len))


