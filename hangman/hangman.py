#!/usr/bin/python3
'''
www.campus.gov.il/self.py - Python programming course - Final exercise
 Student: Elkana Bronstein
 Date: May 2019
 Exercise:
    1. The program gets from the player:
        A. a text file path; The text file contains English word list separated by spaces
        B. an integetr represents the index of a word in the file (*)
    2. The word in the input index in the file will be the secret word the player shall guess
    3. Hangman game starts; At any "stage":
        A. The player will get the status of his progress in the game:
            (i) hangman
            (ii) the secret word
        B. The player will guess a letter (+ repeat until input is valid)
        C. Check weather the input is valid = an English letter that was not guessed previously
            (i)   If the input is invalid print 'X'(**) and repeat 3.B.
            (ii)  If the input is valid and incorrect - print ':(', increment number of tries and repeat 3.A.
            (iii) If the input is valid and correct - check if the player guessed all the secret
                (no) repeat 3.A. without incrementing number of tries
                (yes) print 'WON' and exit

 My addtions:
    (*)  an empty input for the index means a radom index
    (**) The output coloring scheme:
        RED = Wrong input;
        GREEN = Hidden secret word;
        CYAN = Hangman image;            
        BLUE = final result;
        - MAGENTA = DEBUG
'''
# import standard libraries functions
import random
import os
# import other libraries functions (requires installing them)
from colorama import init
from termcolor import colored
# import exercises functions
from ex6 import try_update_letter_guessed
from ex7 import show_hidden_word, check_win
from ex8 import print_hangman
from ex9 import choose_word


COLOR_CODE = {
                "INSTRUCTIONS": 'yellow',            
                "INVALID_INPUT":'red',#('red',['bold']),
                "WORD":'green', 
                "HANGMAN": 'cyan', #('cyan',['bold']),
                "WELCOME": 'blue',
                "RESULT": 'blue', #('blue',['bold']),
                "DEBUG": 'magenta'}

DEBUG_LOGGING = False
DEFAULT_DICTIONARY = "dict.txt"
WELCOME_SCREEN_FILE = "welcome_screen.txt"

def print_debug(message):
    if DEBUG_LOGGING:
        print (colored(message, COLOR_CODE["DEBUG"]))

def print_err_input(message):
        print (colored(message, COLOR_CODE["INVALID_INPUT"]))       
        
def main():
    # print welcome screen
    with open(WELCOME_SCREEN_FILE, 'r') as welcome_file:
        print (colored(welcome_file.read(), COLOR_CODE["WELCOME"]))
    
    # constants
    MAX_TRIES = 7

    # 1. The program gets from the player:
    # 1.A. a text file path; The text file contains English word list separated by spaces
    text_file_path = input("Enter file path: ")
    # 1.B.  an integer represents the index of a word in the file (*)
    index_str = input("Enter index: ")
    # (*) an empty input for the index means a random index
    try:
        secret_word_index = int(index_str)
    except:
        secret_word_index = random.randint(1,1000000)
    print_debug("1. Process input = {0} {1}".format(text_file_path, secret_word_index))
    
    # 2.  The word in the input index in the file will be the secret word the player shall guess
    try:
        secret_word = choose_word(text_file_path, secret_word_index)[1]
    except:
        try:
            text_file_path = DEFAULT_DICTIONARY
            secret_word = choose_word(text_file_path, secret_word_index)[1]
        except:
            print_err_input("Couldn't choose_word from {0} index {1}".format(text_file_path, secret_word_index))
    print_debug("2. Generate secret = {0}".format(secret_word))
    
    # 3. Hangman game starts
    old_letters_guessed = list()
    print (colored("Let's start!", COLOR_CODE["WELCOME"]))
    # main steps loop (including welcome string)
    num_of_tries = 1
    while num_of_tries <= MAX_TRIES:
        # 3.A. The player will get the status of his progress in the game:
        # 3.A.i hangman
        hangman_picture = print_hangman(num_of_tries)
        print (colored(hangman_picture, COLOR_CODE["HANGMAN"]))
        # check end condition for losing the game
        if num_of_tries == MAX_TRIES:
            print_debug("Lose condition met {0} = {1}.format(num_of_tries, MAX_TRIES)")
            # print 'LOST' and exit
            print (colored("LOST", COLOR_CODE["RESULT"]))
            break       
        # 3.A.ii the secret word
        hidden_word = show_hidden_word(secret_word, old_letters_guessed)
        print (colored(hidden_word, COLOR_CODE["WORD"]))
        # check end condition for losing the game
        if check_win(secret_word, old_letters_guessed):
            print_debug("Win condition met - all secret word letters guessed")
            # print 'WON' and exit
            print (colored("WON", COLOR_CODE["RESULT"]))
            break
        # 3.B. The player will guess a letter (repeat until input is valid)
        while True:
            guess_letter_input = input("Guess a letter:")
            # 3.C. Check weather the input is valid
            is_valid = try_update_letter_guessed(guess_letter_input, old_letters_guessed)
            # 3.C.i If the input is invalid print "X" and repeat 3.B.
            if not is_valid:
                print (colored("X", COLOR_CODE["INVALID_INPUT"]))
                continue
            # 3.C.ii If the input is valid and incorrect - print ":(", increment number of tries and repeat 3.A.    
            elif guess_letter_input.lower() not in secret_word.lower():
                print (colored(":(", COLOR_CODE["INVALID_INPUT"]))
                num_of_tries +=1
                print_debug("MISS! tries {0}/{1}. Continue guessing". format(num_of_tries, MAX_TRIES))
                break
            else:
                print_debug("BULLZIE! Continue guessing")
                # repeat 3.A. without incrementing number of tries
                break

    # pre exit - print the secret word (for those who missed it)
    print (colored("The word was {0}".format(secret_word), COLOR_CODE["RESULT"]))

    
#
# Run main
#
if __name__ == "__main__":
    init()
    main()