import random
# print("Let's Play Rock, Paper, Scissors")

player1 = input("[Player 1] Please choose Rock, Paper, Scissors: ")
#Create a list of 3 items
options = ["Rock", "Paper", "Scissors"]

#Generate a random choice
player2 = random.choice(options)

#Print out the variables
# print(f"Player 1 chose {player1} and Player 2 chose {player2}!")

if player1 == player2:
    print("It's a tie!")
elif player1 == "Rock":
    if player2 == "Scissors":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
elif player1 == "Paper":
    if player2 == "Rock":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
elif player1 == "Scissors":
    if player2 == "Paper":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
