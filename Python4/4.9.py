#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename: 4.9.py
#Description: Make a list with the following data ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']. Use a for loop to iterate through each element of this list and: Print out each element. Print out the length and the sequence i.e., "4\tATGC\n"

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for seq in seqs:
	print(len(seq), "\t", seq, "\n")

print("Done.")
