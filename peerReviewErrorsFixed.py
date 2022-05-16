# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Jake Rubin
# Creation Date: 5/14/2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
        print('''You are in a land full of dragons. In front of you, 
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()
	#The above lines between the prints contain errors. Printing the above message with the desired format would appear as follows.
     print('You are in a land full of dragons. In front of you,')
     print('you see two caves. In one cave, the dragon is friendly')
     print('and will share his treasure with you. The other dragon')
     print('is greedy and hungry, and will eat you on sight.')
     print()
        #the printed text would appear awkwardly (randomly indented) without this kind of formatting. The indentation is also off in general.
def chooseCave():
    cave = ''
        while cave != '1' and cave != '2': #This line is an error
    while cave != '1' and cave != '2':
            #the while should be indented to the same level as the above defined cave.
                print('Which cave will you go into? (1 or 2)')
		cave = input() #indendation errors
	print('Which cave will you go into? (1 or 2)')
	cave = input()
	#the indentation matters to the IDLE shell and will not run properly unless correct

	return caves #This line is an error
    return cave
        #we have been talking about "cave", not "caves". "Caves" has not been defined.
        #the return should be indented to the same level as while, which was moved
def checkCave(chosenCave):
	print('You approach the cave...') #this line and following lines appear to contain errors
     print('You approach the cave...')
     #the printed message usually indents at the same place as the checkCave when entered normally. 
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...') #similar indentation error
	#sleep for 2 seconds
	time.sleep(3) #This line is an error
	time.sleep(2)
	#in order to sleep for 2 seconds as noted, it would have to be "2" instead of "3"
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print() #similar indentation errors
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!') #This line is an error
            print('Gives you his treasure!')
            #The indentation is yet again off by a weird margin
	else:
		print 'Gobbles you down in one bite!' #This line is an error
	     print('Gobbles you down in one bite!')
		#parentheses are needed to define what is printed. The indentation need to be correct.

playAgain = 'yes'
while playAgain = 'yes' or playAgain = 'y': #This line is an error
while playAgain == 'yes' or playAgain == 'y':
        #in order to set the while loop's boundaries correctly, 2 equals signs are needed
	displayIntro()
	caveNumber = choosecave() #This line is an error
	caveNumber = chooseCave()
	#The C in Cave needs to be capital like it is in all other areas
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for planing") #line 69 is an error
	    print("Thanks for playing")
		#you play the game, you don't plane it :) The indentation is also off from where it would normally be.

		#the complete code in its correct, smooth, error-free form is below.

import random
import time

def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)


    print('Do you want to play again? (yes or no)')
    playAgain = input()
    if playAgain == "no":
        print("Thanks for playing")
        #the game and the correct code for it can be found at https://inventwithpython.com/chapter6.html 

		

