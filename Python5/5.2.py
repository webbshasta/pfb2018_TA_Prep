#! usr/bin/env python3

#Problemset 5
#Problem 5.1

#Write a script to do the following to Python_05.txt
#	Open and read the contents.
#	Uppercase each line
#	Print each line to the STDOUT

fileObject = open("Python5.txt", "r")
fileWrite = open("Python5.uc.txt", "w")

contents = fileObject.read()

fileWrite.write(contents.upper())

fileObject.close() 

print("Wrote to Python5.uc.txt\n\n\n")
