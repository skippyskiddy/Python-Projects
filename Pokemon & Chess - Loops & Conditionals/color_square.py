'''
   CS5001
   Fall 2022
   Elif Tirkes 
   Homework 3: What color is that square?  
'''
    
def black_or_white(row, column):
    '''
    Function -- black_or_white
        Checks to see if a chessboard square is black or white
        by checking if the row and column are both odd or even
        using modulo. Assumes input is verified.
    Parameters:
       row - the row user input, can take in string or int
       column - the column user input, can take in upper or lower case
    Returns either "BLACK" or "WHITE" depending on the square color 
    '''
    if int(row) % 2 == ord(column) % 2:
        return str("BLACK")
    elif int(row) % 2 != ord(column) % 2:
        return str("WHITE")
    else:
        return False
