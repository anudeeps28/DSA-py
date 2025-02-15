import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    
    wins = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    
    if wins[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = get_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win!")
        else:
            print("Computer wins!")
        
        print()

if __name__ == '__main__':
    play_game()
