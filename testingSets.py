#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename:PS5.1.py

setA = {3, 14, 15, 9, 26, 5, 35, 9}
setB = {60, 22, 14, 0, 9}

intersectionAB = setA & setB

print('The {} between Set A and Set B is {}'.format('intersection', intersectionAB))

differenceAB = setA - setB

print('The {} between Set A and Set B is {}'.format('difference', differenceAB))

unionAB = setA | setB

print('The {} between Set A and Set B is {}'.format('union', unionAB))

symDifferenceAB = setA ^ setB

print('The {} between Set A and Set B is {}'.format('symmetrical difference', symDifferenceAB))
