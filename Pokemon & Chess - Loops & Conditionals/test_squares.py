'''
   CS5001
   Fall 2022
   Elif Tirkes 
   Homework 3: What color is that square?  
'''
from chessboard import check_valid_row
from chessboard import check_valid_column

def main():
    test_squares()
    

def test_column_validity():
    '''
    Function -- test_column_validity
        presents three string-only test cases for the function
        check_valid_column
    Parameters:
        N/A, calls for the check_valid_row and check_valid_column
        with set inputs 
    Returns printed expected and actual results for the 3 tests for
    the check_valid_column function 
    '''   
    col_test_1 = check_valid_column("v")
    col_test_2 = check_valid_column("Z")
    col_test_3 = check_valid_column("B")
    col_test_4 = check_valid_column("A")

    # Column Test 1
    print(f"\n*****\nColumn v: Expected: False, Actual: {col_test_1}")
    # Column Test 2
    print(f"Column Z: Expected: False, Actual: {col_test_2}")
    # Column Test 3
    print(f"Column B: Expected: True, Actual: {col_test_3}")
    # Column Test 4
    print(f"Column A: Expected: True, Actual: {col_test_4}\n*****\n")
    
def test_row_validity():
    '''
    Function -- check_row_validity
        presents three string-only test cases for the function
        check_valid_row
    Parameters:
        N/A, calls for the check_valid_row with set inputs 
    Returns printed expected and actual results for the 3 tests for
    the check_valid_row
    '''    
    row_test_1 = check_valid_row(8)
    row_test_2 = check_valid_row(10)
    row_test_3 = check_valid_row(999)
    row_test_4 = check_valid_row(1)

    # Row Test 1
    print(f"\n*****\nRow 8: Expected: True, Actual: {row_test_1}")
    # Row Test 2
    print(f"Row 10: Expected: False, Actual: {row_test_2}")
    # Row Test 3
    print(f"Row 999: Expected: False, Actual: {row_test_3}")
    # Row Test 4
    print(f"Row 1: Expected: True, Actual: {row_test_4}\n*****\n")
    
def test_squares():
    '''
    Function -- test_squares
       calls test_row_validity() and test_column_validity()
    Returns results for test_row_validity() and test_column_validity() 
    '''
    test_row_validity()
    test_column_validity()


if __name__ == "__main__":
    main() 
