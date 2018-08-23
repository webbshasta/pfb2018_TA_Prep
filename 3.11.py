#!/usr/bin/env python3

import sys

#CSHL Programming for Biology
#Problem 3.11
#Interogate the difference between these two ways to copy a list. Both are not correct.
#	alter the lists after the "copy" by adding a new element to the list
#	print the lists before and after you alter the "copy"

my_list = ['a', 'bb', 'ccc']
print(my_list,'\n')
list_copy = my_list
my_list.append('cat')
print(list_copy, '\n')

my_list = ['a', 'bb', 'ccc']
print(my_list, '\n')
list_copy = my_list.copy()
my_list.append('cat')
print(list_copy, '\n')

#use the copy() method for properly copying lists!



