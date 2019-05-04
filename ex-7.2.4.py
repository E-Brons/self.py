def seven_boom(stop):
    ''' Play "Seven Boom" from 0 to _stop
    :param arg1: ending number
    :type arg1:  int
    :return: None
    '''
    for i in range(stop):
        if ((i%7 ==0) or ("7" in str(i))):
            print ("Boom (" + str(i) +")")
        else:
            print (i)
    
stop = int(input("Please enter an end number:"))
seven_boom(stop)