'''
   CS5001
   Fall 2022
   Elif Tirkes 
   Homework 4: Runlength decoder
'''
def decode(data):
    '''
    Function -- decode()
        Function creates an empty list, and runs through a
        given RLE-encoded dataset, starting with element 0,
        with two steps per loop given that every other item
        on the list is an integer that can
        be used to append the previous item on the list (non integer)
        an x number of times into an 'expanded' new list. 
    Returns a new list of RLE-encoded values with runs expanded 
    '''
    new_list = []
    for i in range(0, len(data), 2):
        for j in range(data[i + 1]):
            new_list.append(data[i])
    return new_list
            
