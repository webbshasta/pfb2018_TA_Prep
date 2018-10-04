#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename: 4.2.py
#Description: Write a script that uses a while loop to calculate the factorial of 1000.

count = 1
factorial = 1
while count < 1001:
	factorial = factorial * count
	count += 1

print("The factorial of 1000 is:", factorial)
print("\n\nDone.")
