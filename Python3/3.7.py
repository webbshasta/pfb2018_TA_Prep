#!/usr/bin/env python3

import sys

#ecoRI site gaattc

seq = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG'

ecoRI = 'GAATTC'

eco_pos = int(seq.find(ecoRI)) + 1

#print('\nThe EcoRI begins at position', eco_pos, 'in', seq)

frag1 = seq[:eco_pos]

frag2 = seq[eco_pos:]

#print('The first and last bases in fragment 1 are:', frag1[0], 'and', frag1[len(frag1) - 1])
#print('The first and last bases in fragment 2 are:', frag2[0], 'and', frag2[len(frag2) - 1])

output = "Fragment 1: {} and begins at position {} and is {} bases long."
output2 = "Fragment 2: {} and begins at position {} and is {} bases long."
print(output.format(frag1, eco_pos - int(len(frag1)), len(frag1)))
print(output2.format(frag2, eco_pos + 1, len(frag2)))



print('Done.\n\n')


