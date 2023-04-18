'''
    Elif Tirkes
    CS 5001, Fall 2022
    Homework  1 - Program 2, ATM

    This is a basic program to calculate minimum bank denominations
    for a desired amount of money.
'''

def main():
    '''
    Below are the test cases:

    Test case #1:
    Input: $5
    Output: 0 fifties, 0 twenties, 0 tens, 1 fives, 0 ones

    Test case #2:
    Input: $78
    Output: 1 fifties, 1 twenties, 0 tens, 5 fives, 3 ones

    Test case #3:
    Input: $503
    Output: 10 fifties, 0 twenties, 0 tens, 0 fives, 3 ones
    '''
    
    amount = int(input("Welcome to PDQ Bank! Amount to withdraw? $ "))

    print(f"Cha-ching! You asked for ${amount}")

    fifties = (amount // 50)
    amount = amount % 50
    twenties = amount // 20
    amount = amount % 20
    tens = amount // 10
    amount = amount % 10
    fives = amount // 5
    amount = amount % 5
    ones = amount // 1

    print("That breaks down to:\n", fifties, "fifties\n", twenties,
          "twenties\n", tens, "tens\n", fives, "fives\n", ones, "ones")

if __name__ == "__main__":
    main()
