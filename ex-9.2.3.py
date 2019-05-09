def who_is_missing(file_name):
    ''' Find missing integer in text file raws
    :param file_name: name of text file containing lists of unsorted integers
    :type arg1:  string
    :return: list of missing numbers of each raw
    :rtype: str
    '''
    COMMA =','
    result = list() # empty list
    # open the given text file
    input_file = open(file_name, 'r')
    # for each line in the file - find the missing int and append to result
    for input_line in input_file:
        # get list of integer strings 
        int_str_list = input_line.replace('\n','').split(COMMA)
        # convert to list of the integers
        int_list = [int(i) for i in int_str_list]
        # find every integer missing from 1 to maximum value in the list
        for i in range(1,max(int_list)):
            if i not in int_list:
                result.append(i)
    # close the text file
    input_file.close()
    # return results
    return result


missings = who_is_missing("ex-9.3.2_inputs.txt")
print(missings)