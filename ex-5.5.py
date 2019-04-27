import random


def is_valid_letter_input(input_string):
    ''' Check validity of input string = a Single English letter
        :param arg1: input string to be validated
        :type arg1:  string
        :return: True if input = a Single English letter; False otherwise
        :rtype: bool
    '''
    is_alpha = input_string.isalpha()
    is_single = (len(input_string)==1)
    if (is_alpha) and (is_single):
        print(input_string.lower())
        return True
    elif (is_alpha) and not (is_single):
        print("E1")
        return False 
    elif not (is_alpha) and (is_single):
        print("E2")
        return False
    else: # not (is_alpha) and not (is_single)
        print("E3")
        return False

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
is_input_valid = is_valid_letter_input(guess_letter_input)
print(is_input_valid)
    