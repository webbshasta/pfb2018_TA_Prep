#!/usr/bin/env python3

import sys

test_seq = 'AATTGGCCA'

#known AT content = 5/9 = 55%

countA = test_seq.count('A')
countT = test_seq.count('T')

countAT = int(countA) + int(countT)

contentAT = (countAT/len(test_seq)) * 100

print('The AT content for the sequence is:', contentAT, '%')

print('\nThis script has finished!\n\n')
