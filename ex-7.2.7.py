def arrow(my_char, max_length):
    ''' Return a string that looks like an arrow of size max_length
    :param arg1: the charachter to build the arrow form
    :type arg1:  string
    :param arg2: maximum number of charachters in a single raw
    :type arg2:  int
    :return: string that looks like an arrow of size max_length
    :rtype: str
    '''
    base_char = my_char + " "
    out_string =""
    for i in range(1, max_length*2):
        if (i < max_length):
            out_string +=  "\n" + base_char * (i)
        else:
            out_string +=  "\n" + base_char * (max_length*2 - i)
    return out_string
    
type = input("Please enter the type charachter:")
size = int(input("Please enter the arrow size:"))
print(arrow(type,size))