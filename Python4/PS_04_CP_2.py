#!/usr/bin/env python3

seq1 = 'CCTCCAAAGCAGGCAGCAGCTCCTCTTCTTCCTAATCACACTATCTCGGA'
seq2 = 'ATTACTATATAAAGTACTGCTGCGAGGCTTGCCG--TGTTGCATTTTGTT'

matches = 0
nonMatches = 0

for position in range(len(seq1)):
	if seq1[position] == seq2[position]:
		matches += 1
	else:
		nonMatches += 1

print('Percent identity between {} and {} is {:.2f}%'.format(seq1, seq2, (matches/(matches + nonMatches))*100))
