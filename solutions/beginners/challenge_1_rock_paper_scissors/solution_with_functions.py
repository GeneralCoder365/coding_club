# PROBLEM STATEMENT:

# WRITE A ROCK PAPER SCISSORS GAME BETWEEN THE USER AND A RANDOMIZED COMPUTER PLAYER

# THE GAME SHOULD TAKE THE PLAYER'S INPUT & COMPARE IT TO THE RANDOMIZED DECISION OF THE COMPUTER (1: rock, 2: paper, 3: scissors)
    # THREE POTENTIAL APPROACHES TO USER INPUT:
        # 1. USER INPUTS "rock", "paper", or "scissors", which is converted to 1, 2, or 3 respectively
        # 2. USER INPUTS 1, 2, or 3, which mean rock, paper, and scissors respectively
        # 3. ACCOUNTS FOR BOTH OPTIONS 1 AND 2

# THE GAME SHOULD DECLARE THE WINNER FOR EACH ROUND
# THE GAME SHOULD CONTINUE UNTIL THE THE PLAYER DOESN'T WANT TO PLAY ANOTHER ROUND

# OPTIONAL: GIVE INFO ON HOW MANY ROUNDS THE GAME HAS GONE ON FOR AND/OR SCORES DATA DURING AND AFTER THE GAME
# OPTIONAL: BE ABLE TO HANDLE NONSENSICAL USER INPUTS



# GENERAL SOLUTION WITH FUNCTIONS (USING INPUT OPTION 3)
# Note that the goal of this solution isn't to make the output look more pretty but show how functions can make code cleaner, faster, and easier to read!

# imports library that will allow for randomization of computer decisions
from random import randint

# initializes necessary variables
player = 0
computer = 0

player_score = 0
computer_score = 0
rounds = 1

continue_play = True

# return: tie --> "tie", player wins --> 0, computer wins --> 1
def who_won_round(player, computer):
    # tie
    if (player == computer):
        return "tie"
    
    # user plays rock
    elif (player == 1):
        # paper beats rock: computer wins
        if (computer == 2):
            return 1
        # rock beats scissors: player wins
        if (computer == 3):
            return 0
    
    # user plays paper
    elif (player == 2):
        # paper beats rock: user wins
        if (computer == 1):
            return 0
        # scissors beats paper: computer wins
        if (computer == 3):
            return 1
        
    # user plays scissors
    elif (player == 3):
        # rock beats scissors: computer wins
        if (computer == 1):
            return 1
        # scissors beats paper: user wins
        if (computer == 2):
            return 0

def who_won_game(player_score, computer_score):
    if (player_score > computer_score):
        print("You win the game!")
    elif (player_score < computer_score):
        print("The computer wins the game!")
    else:
        print("The game has ended in a tie!")

while (continue_play):
    # each round:
    player = input("Rock, Paper Scissors: ")
    computer = randint(1,3)

    # player input conversion to standard [1, 3]
    if ((player.lower() == "rock") or (player == "1")):
        player = 1
    elif ((player.lower() == "paper") or (player == "2")):
        player = 2
    elif ((player.lower() == "scissors") or (player == "3")):
        player = 3
    # handles nonsensical inputs
    else:
        print("Invalid input! Thanks for playing!")
        print()
        print("Rounds: " + str(rounds))
        print()
        print("Final Scores:")
        print("Player: " + str(player_score))
        print("Computer: " + str(computer_score))
        print()
        # who_won_game function application
        who_won_game(player_score, computer_score)
    
    # print player & computer choices
    if (player == 1):
        print("You played rock!")
    elif (player == 2):
        print("You played paper!")
    elif (player == 3):
        print("You played scissors!")
    
    if (computer == 1):
        print("Computer played rock!")
    elif (computer == 2):
        print("Computer played paper!")
    elif (computer == 3):
        print("Computer played scissors!")
    

    # who_won_round function application
    round_winner = who_won_round(player, computer)

    if (round_winner == "tie"):
        print("It's a tie!")
    elif (round_winner == 0):
        print("You won!")
        player_score += 1
    elif (round_winner == 1):
        print("Computer won!")
        computer_score += 1
        

    # play again?
    play_again = input("Would you like to keep playing? [y/n]:")
    print()
    if (play_again.lower() == "y"):
        continue_play = True
    
    else:
        print("Thanks for playing!")
        print()
        print("Rounds: " + str(rounds))
        print()
        print("Final Scores:")
        print("Player: " + str(player_score))
        print("Computer: " + str(computer_score))
        print()
        # who_won_game function application
        who_won_game(player_score, computer_score)
        
        continue_play = False
    
    # increments rounds
    rounds += 1