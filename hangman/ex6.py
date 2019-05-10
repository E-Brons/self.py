#!/usr/bin/python3
from ex5 import check_valid_input
 
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
    if check_valid_input(lowered_input, old_letter_guessed):
        old_letter_guessed += lowered_input
        return True
    else:
        return False