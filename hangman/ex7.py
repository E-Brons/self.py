#!/usr/bin/python3

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
