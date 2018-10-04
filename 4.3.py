#! usr/bin/env/ python3 

#Owner: Shasta Webb
#Filename: 4.3.py
#Description: Iterate through each element of this list using a for loop: [101,2,15,22,95,33,2,27,72,15,52]. Print out only the values that are even (use modulus operator).

nums = [101,2,15,22,95,33,2,27,72,15,52]

for num in nums:
	if num % 2 == 0:
		print(num)

print("\nDone.")	
