import random

options = ["rock", "paper", "scissors"]

player_wins = 0
computer_wins = 0

while player_wins < 3 and computer_wins < 3:

    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    
    player_choice = input("rock, paper, or scissors? ").lower()
    if player_choice not in options:
        print("Invalid choice. Please try again.")
        continue
        
    computer_choice = random.choice(options)
    print(f"You chose {player_choice}. Computer chose {computer_choice}.")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("Player wins!")
        player_wins += 1
    elif player_choice == "paper" and computer_choice == "rock":
        print("Player wins!")
        player_wins += 1
    elif player_choice == "scissors" and computer_choice == "paper":
        print("Player wins!")
        player_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1
        
if player_wins > computer_wins:
    print("Congratulations, you won the game!")
else:
    print("Oh no, the computer won the game. Better luck next time!")
