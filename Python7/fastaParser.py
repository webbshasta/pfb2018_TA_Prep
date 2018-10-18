#!/usr/bin/env python3

#Open and print the reverse complement of each sequence in Python_05.fasta. Make sure to print the output in fasta format including the sequence name and a note in the description that this is the reverse complement. Print to STDOUT and capture the output into a file with a command line redirect '>'.k
#Refer to PS 3.3.py for reverse comple
fasta_read = open('Python_07.fasta', 'r')

fasta_seqs = {}
fasta_keys = None

for line in fasta_read:
	line = line.rstrip()
	if line.startswith('>'):
		line = line.replace('>', '')
		fasta_keys = line
		fasta_seqs[fasta_keys] = ''
	else:
		fasta_seqs[fasta_keys] += line

print(fasta_seqs)
fasta_read.close()
