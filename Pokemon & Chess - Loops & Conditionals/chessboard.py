'''
   CS5001
   Fall 2022
   Elif Tirkes 
   Homework 3: What color is that square?
'''
def main():
    get_row = input("What row is the chess square in?: ")
    get_column = str(input("What column is the chess square in?: "))
    print(check_valid_row(get_row))
    print(check_valid_column(get_column))
    print(black_or_white(get_row, get_column))

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

def check_valid_row(row):
    '''
    Function -- check_valid_row
        Checks to see if the input of the row is valid.
        While it can take in a string, it will return false
        if the row input is not a valid integer between 1 and 8 
    Parameters:
       row - the row user input, can take in string or int

    Returns either "True" or "False" depending on input validity 
    '''
    # turns string integers into int type integers
    if type(row) == str:
        row = int(row)
    if int(row) >= 1 and int(row) <= 8:
        return True
    else:
        return False

def check_valid_column(column):
    '''
    Function -- check_valid_column
        Checks to see if the input of the column is valid.
        Can take in an upper or lower case input. Returns false
        for non-string inputs. 
    Parameters:
       columb - the column user input, can take in string

    Returns either "True" or "False" depending on input validity 
    '''
    if int(ord(column)) >= 65 and int(ord(column)) <= 72:
        return True
    elif int(ord(column)) >= 97 and int(ord(column)) <= 104:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
