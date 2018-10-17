#! usr/bin/env/ python3

#Owner: Shasta Webb
#Filename:PS5.1.p value from the command line for fav_thing and print the value of that item from the dictionary. Maybe you want to print out all the keys to the user so that they know what to pick from.
#Description:  

favs = {
		'book' : 'Lonesome Dove',
		'song' : 'Only Skin',
		'tree' : 'BSIM',
		'organism' : 'cat'
		}

keyOptions = []

for key in favs.keys():
	keyOptions.append(key)

print(keyOptions)

chosen = input("From the list of items above, in which category would you like to designate a favorite? Type your answer on the command line.\n")

if chosen in keyOptions:
	favThing = input("What is your favorite thing in the category you chose?\n")
	favs[chosen] = favThing

print(favs)

print('\nDone.\n')




 
