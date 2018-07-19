#!/usr/bin/env python3

import sys

user_input = int(sys.argv[1])

if user_input > 0:
	if user_input > 50:
		if user_input % 3 == 0:
			print(user_input, "is greater than 50, and divisible by 3.")
		else:
			print(user_input, "is greater than 50, but is not divisble by 3.") 
	elif user_input < 50:
		if user_input % 2 == 0:
			print(user_input, "is smaller than 50, and is an even number.")
		else:
			print(user_input, "is smaller than 50, but is an odd number.")
else:
	print(user_input, "is a negative number.\n")  


print("End of script.\n\n")
