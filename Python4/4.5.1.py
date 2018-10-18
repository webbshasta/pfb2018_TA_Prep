#! usr/bin/env/ python3 

#Owner: Shasta Webb
#Filename: 4.5.1.py
#Description: Create a new script that uses list comprehension to do the same, uses range to print out every number bewteen 1 and 100.

nums = [num for num in range(0,100) if num % 2 == 0]

print(nums)

print("\nDone.")
