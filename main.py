import random

OPTIONS = ('rock', 'paper', 'scissor')

def get_user_option():
    while True:
        user_option = input('Rock, Paper, Scissors => ').lower()
        if user_option in OPTIONS:
            return user_option
        print('Invalid option. Please choose Rock, Paper, or Scissor.')

def determine_winner(user_option, bot_option):
    if user_option == bot_option:
        return 'Draw'
    elif (user_option == 'rock' and bot_option == 'scissor') or \
         (user_option == 'paper' and bot_option == 'rock') or \
         (user_option == 'scissor' and bot_option == 'paper'):
        return 'User'
    else:
        return 'Bot'

def play_round():
    user_option = get_user_option()
    bot_option = random.choice(OPTIONS)
    
    print(f'Player => {user_option}')
    print(f'Bot => {bot_option}')
    
    print("*" * 30)
    
    winner = determine_winner(user_option, bot_option)
    if winner == 'Draw':
        print('Draw')
    else:
        print(f'{winner} wins this round!')
    
    print("*" * 30)

    return winner

def main():
    print("*" * 30)
    print("Rock - Paper - Scissors (Armonia Push Game)")
    print("Start Game")
    print("*" * 30)
    
    user_wins = 0
    bot_wins = 0

    while user_wins < 3 and bot_wins < 3:
        winner = play_round()
        if winner == 'User':
            user_wins += 1
        elif winner == 'Bot':
            bot_wins += 1

    print("*" * 30)
    print('Game Over')
    print('User wins the game!' if user_wins > bot_wins else 'Bot wins the game!')

    play_again = input('Do you want to play again? (yes/no): ').lower()
    if play_again == 'yes':
        main()

if __name__ == "__main__":
    main()