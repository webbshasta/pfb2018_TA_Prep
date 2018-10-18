#! usr/bin/env/ python3

#Open the FASTQ file Python_05.fastq and go through each line of the file. Count the number of lines and the number of characters per line. Have your program report the:
#	total number of lines
#	total number of characters
#	average line length

#PS 5. Problem 5.4

fo = open("Python5.fastq", "r")

numberLines = 0
numberCharacters = []
aveLineLength = []

for line in fo:
	#line = line.rstrip()
	numberLines += 1
	numberCharacters.append(len(line)) 
	aveLineLength.append(len(line)) 

fo.close()

print("Number of lines in file:\t", numberLines, "\nNumber of characters in file:\t", sum(numberCharacters), "\nAverage line length:\t\t", sum(aveLineLength)/len(aveLineLength))

print("\nDone.")
