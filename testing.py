#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename:PS5.1.py


favs = {
		'book' : 'Lonesome Dove',
		'song' : 'Only Skin',
		'tree' : 'pine',
		'organism' : 'cat'
		}

newOrganism = input("What is your favorite organism?\n\n")

favs['organism'] = newOrganism

print(favs)

print('\nDone.\n')
