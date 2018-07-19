#!/usr/bin/env python3

import sys

user_input = sys.argv[1]

if bool(user_input) is False:
	print(user_input, "is false.")
else: 
	print(user_input, "is true.")

print("End of script.\n")


