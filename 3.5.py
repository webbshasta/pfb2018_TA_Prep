#!/usr/bin/env python3

import sys

#ecoRI site gaattc

seq = 'AAAAAGAATTCAAAAA'

ecoRI = 'GAATTC'

eco_pos = seq.find(ecoRI)

print('The EcoRI begins at position', eco_pos, 'in', seq)

print('Done.\n\n')


