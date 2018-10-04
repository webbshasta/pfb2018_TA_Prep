#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename: 4.7.py
#Description: Rewrite the script to take to start and end values from the command line. If you call your script like this count.py 3 10 it will print the numbers from 3 to 10.

#note: To ensure that the code interprets command line arguments as integers, you have to specify that. Otherwise the default is string.

import sys

startNum = int(sys.argv[1])
endNum = int(sys.argv[2]) + 1

for i in range(startNum,endNum):
	print(i)

print("\nDone.")


