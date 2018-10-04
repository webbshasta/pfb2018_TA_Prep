#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename: 4.4.py
#Description: Sort the elements of the above list, then iterate through each element using a for loop and: Print each element, Calculate two cumulative sums, one of all the even values and one of all the odd values, Print the only the final two sums.

nums = [101,2,15,22,95,33,2,27,72,15,52]
evens = []
odds = []

for num in sorted(nums):
	print(num)
	if num % 2 == 0:
		evens.append(num)
	else:
		odds.append(num)

print("Sum of numbers:", sum(nums), "Sum of even numbers:", sum(evens), "\nSum of odds:", sum(odds))

print("\n\nDone.")



