import random


##
## Welcome screen
##
# read and print welcome screen txt file
hangman_welcome_screen_file = open('hangman_welcome_screen.txt', 'r')
HANGMAN_ASCII_ART = hangman_welcome_screen_file.read()
print(HANGMAN_ASCII_ART)

##
## Get random number of guesses
##

MAX_TRIES = random.randint(5,10)
print(MAX_TRIES)

##
## Start playing: input guess string
##
guess_word_input = input("Please enter a word:")
print(" _"* len(guess_word_input))

guess_letter_input = input("Guess a letter:")
if (guess_letter_input.isalpha()==True) and (len(guess_letter_input)==1):
    guess_letter_input = guess_letter_input.lower()
    print(guess_letter_input)
else:
    print("Wrong input", guess_leter_input)
