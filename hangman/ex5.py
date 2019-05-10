#!/usr/bin/python3
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