def squared_numbers(start, stop):
    ''' Return list of square numbers from Start to End
    :param arg1: starting number
    :type arg1:  int
    :param arg2: ending number
    :type arg2:  int
    :return: list of squared numbers
    :rtype: list
    '''
    squared_list = list()
    while (start <= stop):
        squared_list += [start**2]
        start += 1
    return squared_list
    
start = int(input("Please enter a start number:"))
stop = int(input("Please enter an end number:"))
print(squared_numbers(start,stop))