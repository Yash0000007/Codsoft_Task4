import random

def determine_winner(user, com):
    if user == com:
        return "It's a tie!"
    elif (
        (user == 'rock' and com == 'scissors') or
        (user == 'scissors' and com == 'paper') or
        (user == 'paper' and com == 'rock')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nWelcome to Rock-Paper-Scissors!")
        print("Choose your move: rock, paper, or scissors")
        user = input().lower()
        
        if user not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        com = random.choice(['rock', 'paper', 'scissors'])
        
        print(f"\nYou chose: {user}")
        print(f"Computer chose: {com}")
        
        result = determine_winner(user, com)
        print(result) 
        
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        print(f"\nScore - You: {user_score}, Computer: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
