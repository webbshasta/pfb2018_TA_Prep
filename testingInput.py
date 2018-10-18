#! usr/bin/env/ python3

import sys

#Owner: Shasta Webb
#Filename:PS5.1.py


favs = {
		'book' : 'Lonesome Dove',
		'song' : 'Only Skin',
		'tree' : 'pine',
		'organism' : 'cat'
		}
		
#newFavKey = sys.argv[1]

#newFavValue = input("What is your favorite "+ newFavKey + " ?\n\n")

#favs[newFavKey] = newFavValue

for k, v in favs.items():
	print(k + ':' + v)


print(favs)

print('\nDone.\n')
