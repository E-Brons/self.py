#!/usr/bin/python3
import random
import hangman_picture


def is_valid_letter_input(input_string, old_letter_guessed):
    """ Check validity of input string = a Single English letter
        :param input_string: input string to be validated
        :type input_string:  string
        :param old_letter_guessed: list of letters that were previously guessed
        :type old_letter_guessed:  list
        :return: True if input = a Single English letter; False otherwise
        :rtype: bool
    """
    is_alpha = input_string.isalpha()
    is_single = (len(input_string)==1)
    lowered_input = input_string.lower()
    if (is_alpha) and not (is_single):
        # print("E1")
        return False 
    elif not (is_alpha) and (is_single):
        # print("E2")
        return False
    elif not (is_alpha) and not (is_single):
        # print("E3")
        return False
    elif lowered_input in old_letter_guessed:
        # print("E4")
        return False
    else:  # (is_alpha) and (is_single) + not guessed earlier
        print(lowered_input)
        return True


def try_update_letter_guessed(input_string, old_letter_guessed):
    """ update letter_guessed list if input is valid (see is_valid_letter_input)
        :param input_string: input string to be validated
        :type input_string:  str
        :param old_letter_guessed: list of letters that were previously guessed
        :type old_letter_guessed:  list
        :return: True if list updated
        :rtype: bool
    """
    lowered_input = input_string.lower()
    if is_valid_letter_input(lowered_input, old_letter_guessed):
        old_letter_guessed += lowered_input
        return True
    else:
        return False


def show_hidden_word(secret_word, letters_guessed):
    """ create a string, disclosing only the guessed letters out of the secret word and the gaps 
        :param secret_word: secret string
        :type secret_word:  str
        :param letters_guessed: list of letters that were previously guessed
        :type letters_guessed:  list
        :return: string partially disclosing the secret word and underlines in the gaps
        :rtype: str
    """
    out_str = ""
    for secret_char in secret_word:
        if secret_char.lower() in letters_guessed:
            out_str += secret_char + " "
        else:
            out_str += "_ "
    return out_str


def check_win(secret_word, letters_guessed):
    """ check if letter guessed disclose the whole secret word
        :param secret_word: secret string
        :type secret_word:  str
        :param letters_guessed: list of letters that were previously guessed
        :type letters_guessed:  list
        :return: Whether the secret word guessed
        :rtype: bool
    """
    for secret_char in secret_word:
        if not secret_char.lower() in letters_guessed:
            return False
    # all secret_chars were guessed
    return True

def main():
    #
    # Welcome screen
    #
    # read and print welcome screen txt file
    hangman_welcome_screen_file = open('hangman_welcome_screen.txt', 'r')
    HANGMAN_ASCII_ART = hangman_welcome_screen_file.read()
    print(HANGMAN_ASCII_ART)

    #
    # Get random number of guesses
    #

    MAX_TRIES = random.randint(5,9)
    print(MAX_TRIES)

    #
    # Start playing: input guess string
    #
    guess_word_input = input("Please enter a word:")
    print(" _"* len(guess_word_input))

    #
    # input guess letter
    #
    previously_guessed_letters = list()
    num_of_tries = 0
    while num_of_tries < MAX_TRIES:
        guess_letter_input = input("Guess a letter:")
        is_input_valid = try_update_letter_guessed(guess_letter_input, previously_guessed_letters)
        print(is_input_valid)
        print(show_hidden_word(guess_word_input, previously_guessed_letters))
        if guess_letter_input.lower() in guess_word_input.lower():
            if check_win(guess_word_input, previously_guessed_letters):
                print("You won!")
                return None
        else:
            num_of_tries +=1
            hangman_picture.print_hangman(num_of_tries)

    # num_of_tries exausted - game over
    print("You are hanged and DEAD!")
    print("Please come back in your next life")
    print("--- GAME OVER ---")

#
# Run main
#
if __name__ == "__main__":
    main()
