'''
   CS5001
   Fall 2022
   Elif Tirkes 
   Homework 4: UPC Detector 
'''

def main():
    print(is_valid_upc([0, 7, 3, 8, 5, 4, 0, 0, 8, 0, 8, 9]))
    # calls function to check if string is a valid upc 


def is_valid_upc(list_of_integers):
    '''
    Function -- is_valid_upc()
        Function takes in list of integers,
        sets a counter starting from 0.
        Running through the list from right to
        left, if the integer
        is in an even position, it multiplies it
        by 3 and adds it to count variable.
        If the integer is in an odd position, it
        simply adds the number
        to the count variable.
        If the total count is divisible by 10,
        the upc number is valid.
        Function also checks to see if the
        length of the input is less than 2
        (in which case it returns false),
        and if all the digits are 0 (where
        it also would return false).              
    Parameters:
    list_of_integers -- a list of integers representing
    a upc number 
    Returns a boolean value True or False depending on
    whether it satisfies the upc checking algorithm
    '''
    
    length = len(list_of_integers)
    
    if length >= 2 and sum(list_of_integers) > 0:

        count = 0
        
        for i in range(length - 1, 0, -1): 
            # moves through the list in reverse
            # by starting at length - 1 and moving by -1 steps

            if i % 2 == 0:
                # if number is in an even position
                count = count + list_of_integers[i] * 3

            else:
                # if number is in an odd position 
                count = count + list_of_integers[i]

        if count % 10 == 0:
            # if the sum of all numbers are divisible by 10
            # returns True
            return True                       

        else:
            # if not divisible by 10, not valid UPC
            return False
                
    else:
        # if length is less than 2 number and sum of all numbers
        # equals to 0, not a valid UPC
        return False
    
if __name__ == "__main__":
    main() 
