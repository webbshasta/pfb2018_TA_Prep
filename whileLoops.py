#! usr/bin/env python3

#While loop and continue practice

count = 0

while count < 5:
	print("count:", count)
	count += 1
	if count == 3:
		continue
	print("line after continue")
print("Done")
