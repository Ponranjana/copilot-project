import random

# Define the possible choices and rules
CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
RULES = {
    ("scissors", "lizard"): "Scissors decapitate lizard",
    ("scissors", "paper"): "Scissors cuts paper",
    ("paper", "rock"): "Paper covers rock",
    ("rock", "lizard"): "Rock crushes lizard",
    ("lizard", "spock"): "Lizard poisons Spock",
    ("spock", "scissors"): "Spock smashes scissors",
    ("lizard", "paper"): "Lizard eats paper",
    ("paper", "spock"): "Paper disproves Spock",
    ("spock", "rock"): "Spock vaporizes rock",
    ("rock", "scissors"): "Rock crushes scissors",
}

def get_user_choice():
    """Prompt the user to select an option."""
    print("Choose one of the following:")
    for i, choice in enumerate(CHOICES, 1):
        print(f"{i}. {choice.capitalize()}")
    while True:
        try:
            user_input = int(input("Enter the number of your choice: "))
            if 1 <= user_input <= len(CHOICES):
                return CHOICES[user_input - 1]
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice():
    """Randomly select an option for the computer."""
    return random.choice(CHOICES)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the rules."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice, computer_choice) in RULES:
        return f"You win! {RULES[(user_choice, computer_choice)]}"
    else:
        return f"You lose! {RULES[(computer_choice, user_choice)]}"

def main():
    """Main function to run the game."""
    print("Welcome to Rock Paper Scissors Lizard Spock!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        print(determine_winner(user_choice, computer_choice))
        
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()