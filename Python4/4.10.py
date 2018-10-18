#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename: 4.10.py
#Description: Use list comprehension to generate a list of tuples of sequences and lengths with the list from #9. Print out the length and the sequence i.e., "4\tATGC\n".

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

lengths = [(seqs.index(seq), len(seq), seq) for seq in seqs] 

#print(lengths)

for length in lengths:
	print(length[0], "\t", length[1], "\t", length[2])


print("Done.")
