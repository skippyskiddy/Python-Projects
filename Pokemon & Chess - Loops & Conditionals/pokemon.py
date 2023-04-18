'''
   CS5001
   Fall 2022
   Elif Tirkes 
   Homework 3: Pokemon 
'''

import random

def main():
    computer_score = 0
    user_score = 0
    # sets the user and computer score to 0 

    user_team_selection = str(input("What team do you want(Red or Blue)? :"))
    # asks the user for team selection 
    computer_team_selection = team_picking(user_team_selection)
    # calls for function team_picking to assign
    # the opposing team for the computer based
    # on the user's team selection 
    user_pokemon = get_player(random.randint(0, 10))
    # picks a random pokemon for the user using randint 
    computer_pokemon = get_player(random.randint(0, 10))
    # picks a random pokemon for the computer using randint 
    print(f"{user_team_selection.upper()} pokemon {user_pokemon} \
    vs. {computer_team_selection} pokemon {computer_pokemon}")

    user_rps_number = int(input("Enter 1 for Rock, \
    2 for Paper, 3 for Scissors: "))
    # asks user for their Rock, Paper, or Scissors choice with int inputs 
    computer_rps_number = int(random.randint(1, 3))
    # randomly assigns the computer a Rock, Paper, or Scissors value
    
    user_rps_selection = number_to_rps_string(user_rps_number)
    computer_rps_selection = number_to_rps_string(computer_rps_number)
    # converts user and computer
    # integer Rock, Paper, Scissors selection
    # to its string value using number_to_rps_string function
    print(f"{user_pokemon} played {user_rps_selection}. \
    {computer_pokemon} played {computer_rps_selection}")
    
    result = str(check_battle(computer_rps_number, user_rps_number))
    # compares the user and computer's RPS value
    # to determine the value, stores the
    # winner in "result" as a string 
    if result == "COMPUTER":
        computer_score += 1
    elif result == "PLAYER":
        user_score += 1
    # adds a score for the user
    # or the computer based on
    # the return value stored in "result"
        
    score_printing(result, computer_team_selection,
                   computer_pokemon, user_team_selection,
                   user_pokemon)
    # prints the results to user 

    play_again = str(input("Play again? (y/n): "))
    # asks user to play again for round 1 

    while play_again == "y":
        # begins a loop to continue playing
        # with above functions as long as the user responds "y"  
        user_rps_number = int(input("Enter 1 for Rock, \
        2 for Paper, 3 for Scissors: "))
        computer_rps_number = int(random.randint(1, 3))
        user_rps_selection = number_to_rps_string(user_rps_number)
        computer_rps_selection = number_to_rps_string(computer_rps_number)
        print(f"{user_pokemon} played {user_rps_selection}. \
        {computer_pokemon} played {computer_rps_selection}")
        result = str(check_battle(computer_rps_number, user_rps_number))
        if result == "COMPUTER":
            computer_score += 1
        elif result == "PLAYER":
            user_score += 1
 
        score_printing(result, computer_team_selection,
                       computer_pokemon, user_team_selection,
                       user_pokemon)
        play_again = str(input("Play again? (y/n): "))

    else:
        # if the users answers "n" to play again,
        # prints the winning results calculated
        # in user_score and computer_score 
        print(f"Tournament has ended! \n*****\n \
        {user_team_selection.upper()} : {user_score} \n*****\n \
        {computer_team_selection} : {computer_score}")
        check_winner(computer_score, user_score,
                     user_team_selection, computer_team_selection)
        # check_winner function compares the values
        # of user_score and computer_score to determine the winner 

def number_to_rps_string(num):
    '''
    Function -- number_to_rps_string 
        converts the rock paper scissors
        input value (1-3) to its string equivalent 
    Parameters:
        num - int between 1-3 representing
        rock, paper, or scissors 
    Returns a string value representing
    the RPS equivalent of the integer 
    '''
    if num == 1:
        return "ROCK"
    elif num == 2:
        return "PAPER"
    elif num == 3:
        return "SCISSORS"
    else:
        print("Please give a valid input between 1-3")
        
def team_picking(team):
    '''
    Function -- team_picking
        takes in the user's preference for
        team red or blue, and assigns the
        opposite team for the computer 
    Parameters:
        team -- string "red" or "blue"
        representing team preference 
    Returns a string value with the computer's assigned team 
    '''
    if team.upper() == "BLUE":
        return "RED"
    elif team.upper() == "RED":
        return "BLUE"
    else:
        print("Please give a valid input")

def get_player(num):
    '''
    Function -- get_player
        converts the randomized integer value
        for the user and computer into a
        pokemon assigned to integers 1-8.
        If integer is out of bounds,
        returns the default pokemon Diglett. 
    Parameters:
        num -- int between 1-10 picked
        using randint from the imported random package 
    Returns a string value representing
    the matching assigned pokemon for the input integer 
    '''
    if num == 1: 
        return "Bulbasaur"
    if num == 2:
        return "Charmander"
    if num == 3:
        return "Butterfree"
    if num == 4:
        return "Rattata"
    if num == 5:
        return "Weedle"
    if num == 6:
        return "Pikachu"
    if num == 7:
        return "Sandslash"
    if num == 8:
        return "Jigglypuff"
    if num == 9:
        return "Raichu"
    else:
        return "Diglett"

def check_battle(computer, player):
    '''
    Function -- check_battle
        compares the user input for RPS game
        with the computer's randomized input for RPS.
        if input value wins, returns string "PLAYER"
        to indicate that player wins the round.
        Otherwise, returns "COMPUTER" if computer's
        RPS choice wins the round.
        returns "DRAW" if both user and computer
        played for the same RPS values.
    Parameters:
        user -- integer storing input RPS
        choice from the user
        computer -- integer storing
        randomized RPS choice for the computer 
    Returns a string value representing the winner of each round 
    '''
    if player == computer:
        return "DRAW!"
    # user input rock, computer scissors
    elif player == 1:
        if computer == 3:
            return "PLAYER"
        # user input rock, computer paper
        else:
            return "COMPUTER"
    elif player == 2:
        # user input paper, computer rock
        if computer == 1:
            return "PLAYER"
        # user input paper, computer scissors
        else:
            return "COMPUTER"
    elif player == 3:
        # user input scissors, computer paper
        if computer == 2:
            return "PLAYER"
        # user input scissors, computer rock
        else:
            return "COMPUTER"

def score_printing(result, computer_team_selection, 
                   computer_pokemon, user_team_selection, user_pokemon):
    '''
    Function -- score_printing
        prints the results for each round of
        rock,paper,scissors using the user
        and computer's team and pokemon selection 
    Parameters:
        result -- string value storing the
        winner for the round, either "COMPUTER",
        "PLAYER", or "DRAW" for no winner 
        computer_team_selection -- inputs the
        string for computer's team RED or BLUE
        to return in print function 
        computer_pokemon -- inputs the string
        for computer's pokemon to return in
        print function 
        user_team_selection -- inputs the string
        for user's team RED or BLUE to return in
        print function 
        user_pokemon -- inputs the string for
        user's pokemon to return in print function 
    Returns a printed string sentence nesting 
    the user or computer's team and
    pokemon selection, and determined winner
    '''
    if result == "COMPUTER":
        print(f"my {computer_team_selection} \
        team wins with {computer_pokemon}!")
    elif result == "PLAYER":
        print(f"my {user_team_selection.upper()} \
        team wins with {user_pokemon}")
    elif result == "DRAW!":
        print(f"it's a draw! No winner")
    else:
        print(f"invalid input")
    
def check_winner(computer_score, user_score, 
                 user_team_selection, computer_team_selection):
    '''
    Function -- check_winner
        compares the computer_score and
        user_score value when prompted,
        returns the determined winner in
        a printed string sentence depending
        on which of the
        two scores is greater, or indicates a
        draw if both score values are equivalent.
    Parameters:
        computer_score -- integer value summing
        the tallied score for each round that
        the computer was determined winner 
        user_score -- integer value summing
        the tallied score for each round
        that the user was determined winner 
        user_team_selection -- string value
        storing the user's team selection RED or BLUE 
        computer_team_selection --  string
        value storing the computer's team
        selection RED or BLUE
    Returns a printed string sentence
    announcing the winner of the RPS game 
    '''
    if computer_score < user_score:
        print(f"{user_team_selection} WINS!")
    elif computer_score > user_score:
        print(f"{computer_team_selection} Computer WINS!\n")
    else:
        print(f"it's a DRAW!")

if __name__ == "__main__":
    main()
