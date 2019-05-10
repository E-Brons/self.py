def choose_word(file_name, n_):
    ''' return the number of unique words AND #n__th word in a text file containing words only
    :param file_name: name of text file containing lists of words (may include repetitions)
    :type file_name:  string
    :param n_: index of the word in a list of unique words in the file [1,n_words]
    :type n_:  int
    :return: number of unique words in the file + the chosen word
    :rtype: tuple
    '''
    # use a map's key uniqueness to count only unique words
    word_map = {}
    
    # open the given text file
    with open(file_name, 'r') as input_file:
        # for each line in the file - find the missing int and append to result
        word_list = input_file.read().split()
        for word in word_list:
            word_map[word] = 0 # the key is important, value is arbitrary an unused 
    # convert the map keys to a list
    unique_word_list = list(word_map.keys())
    # use the index according to exercise definition [1-n_words] with wraparound
    index = (n_ -1 ) % len(word_list)
    # return the requested word
    return len(unique_word_list) , word_list[index]

##
## Test 
##
print(choose_word("ex-9.4_input.txt", 3))
print(choose_word("ex-9.4_input.txt", 15))