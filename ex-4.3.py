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

##
## input guess letter
##
guess_letter_input = input("Guess a letter:")
is_alpha = guess_letter_input.isalpha()
is_single = (len(guess_letter_input)==1)

if (is_alpha) and (is_single):
    guess_letter_input = guess_letter_input.lower()
    print(guess_letter_input)
elif (is_alpha) and not (is_single):
    print("E1")
elif not (is_alpha) and (is_single):
    print("E2")
else: # not (is_alpha) and not (is_single)
    print("E3")
	