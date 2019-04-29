import random

def is_valid_letter_input(input_string, old_letter_guessed):
    ''' Check validity of input string = a Single English letter
        :param arg1: input string to be validated
        :type arg1:  string
        :param arg2: list of letters that were previously guessed
        :type arg1:  list
        :return: True if input = a Single English letter; False otherwise
        :rtype: bool
    '''
    is_alpha = input_string.isalpha()
    is_single = (len(input_string)==1)
    lowered_input = input_string.lower()
    if (is_alpha) and not (is_single):
        #print("E1")
        return False 
    elif not (is_alpha) and (is_single):
        #print("E2")
        return False
    elif not (is_alpha) and not (is_single):
        #print("E3")
        return False
    elif lowered_input in old_letter_guessed:
        #print("E4")
        return False
    else: # (is_alpha) and (is_single) + not guessed earlier
        print(lowered_input)
        return True

def try_update_letter_guessed(input_string, old_letter_guessed):
    ''' update letter_guessed list if input is valid (see is_valid_letter_input)
        :param arg1: input string to be validated
        :type arg1:  string
        :param arg2: list of letters that were previously guessed
        :type arg1:  list
        :return: True if list updated
        :rtype: bool
    '''
    lowered_input = input_string.lower()
    if is_valid_letter_input(lowered_input, old_letter_guessed):
        old_letter_guessed += lowered_input
        return True
    else:
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
previously_guessed_letters = list()

guess_letter_input = input("Guess a letter:")
is_input_valid = try_update_letter_guessed(guess_letter_input, previously_guessed_letters)
print(is_input_valid)
