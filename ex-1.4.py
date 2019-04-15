import random


##
## Welcome screen
##
# read and print welcome screen txt file
f = open('hangman_welcome_screen.txt', 'r')
welcome_screen_txt = f.read()
print(welcome_screen_txt)

##
## Get random number of guesses
##

max_guesses = random.randint(5,10)
print(max_guesses)
