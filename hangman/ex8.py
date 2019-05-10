from termcolor import colored

HANGMAN_PHOTOS = {
    1: ["x-------x"],
    2: ["x-------x",
        "|        ",
        "|        ",
        "|        ",
        "|        ",
        "|        "],
    3: ["x-------x",
        "|       |",
        "|       0",
        "|        ",
        "|        ",
        "|        "],
    4: ["x-------x",
        "|       |",
        "|       0",
        "|       |",
        "|        ",
        "|        "],        
    5: ["x-------x",
        "|       |",
        "|       0",
        "|      /|\\",
        "|        ",
        "|        "],  
    6: ["x-------x",
        "|       |",
        "|       0",
        "|      /|\\",
        "|      / ",
        "|        "],  
    7: ["x-------x",
        "|       |",
        "|       0",
        "|      /|\\",
        "|      / \\",
        "|        "]}
        
def print_hangman(num_of_tries, color = 'white'):
    """
    return a picture describing number of tries
    :param num_of_tries: number of wrong tries
    :type num_of_tries: int
    :return: a string which describes the number of tries
    :rtype: str
    """
    output =""
    for line in HANGMAN_PHOTOS[num_of_tries]:
        output += line + "\n"
    return output