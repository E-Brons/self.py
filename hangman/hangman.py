#!/usr/bin/python3
# import libraries functions
import random
from termcolor import colored
# import exercises functions
from ex8 import print_hangman
from ex9 import choose_word

'''
www.campus.gov.il/self.py - Python programming course - Final exercise
 Student: Elkana Bronstein
 Date: May 2019
 Exercise:
     1. The program gets from the player:
         A. a text file path; The text file contains English word list separated by spaces
         B. an integetr represents the index of a word in the file (*)
     2. The word in the input index in the file will be the secret word the player shall guess
     3. From this point, the game will follow "hangman" rules:
         A. At any "stage" the player will guess a letter
         B. The player will get reply weather the input is valid(**)
         C. The player will get the status of his progress in the game
         D. In case of wrong guess (as oppose to invalid input) progress will be in the form of hangman image

 My addtions:
     (*)  an empty input for the index means a radom index
     (**) The output coloring scheme:
           GRAY/WHITE = player input;
           YELLOW = instructions ;
           RED = Wrong input;
           GREEN = Positive progress;
           CYAN = Negative (Hangman image) progress;            
           BLUE = final result;
           - MAGENTA = DEBUG
'''

COLOR_CODE = {
                "INSTRUCTIONS": 'yellow',            
                "WRONG_INPUT":'red',#('red',['bold']),
                "WORD":'green', 
                "HANGMAN": 'cyan', #('cyan',['bold']),
                "WELCOME": 'blue',
                "RESULT": 'blue', #('blue',['bold']),
                "DEBUG": 'magenta'}

DEBUG_LOGGING = True
WELCOME_SCREEN_FILE = 'welcome_screen.txt'

def print_debug(message):
    if DEBUG_LOGGING:
        print (colored(message, COLOR_CODE["DEBUG"]))

def print_err_input(message):
        print (colored(message, COLOR_CODE["WRONG_INPUT"]))       
        
def main():
    # print welcome screen
    with open(WELCOME_SCREEN_FILE, 'r') as welcome_file:
        print (colored(welcome_file.read(), COLOR_CODE["WELCOME"]))
    
    # constants
    MAX_TRIES = 7

    # 1. The program gets from the player:
    # 1.A. a text file path; The text file contains English word list separated by spaces
    text_file_path = input(colored ("Enter file path:", 'yellow'))
    # 1.B.  an integetr represents the index of a word in the file (*)
    index_str = input(colored ("Enter index:", 'yellow'))
    # (*) an empty input for the index means a radom index
    try:
        secret_word_index = int(index_str)
    except:
        secret_word_index = random.randint(1,1000000)
    print_debug("{0} {1}".format(text_file_path, secret_word_index))
    
    # process (1) inputs
    try:
        unused, secret_word = choose_word(file_name, secret_word_index)[1]
    except:
        print_err_input("Couldn't choose_word from {0} index {1}".format(text_file_path, secret_word_index))
        
    # main steps loop (including welcome string)
    for num_of_tries in range(MAX_TRIES):
        pass
        #print_hangman(num_of_tries, COLOR_CODE["HANGMAN'])

#
# Run main
#
if __name__ == "__main__":
    main()