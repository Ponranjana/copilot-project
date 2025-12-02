import random

def get_computer_choice():
    """Get a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the round."""
    if user_choice == computer_choice:
        return "tie"
    
    win_conditions = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if win_conditions[user_choice] == computer_choice:
        return "win"
    return "lose"

def display_result(user_choice, computer_choice, result):
    """Display the round result with emoji."""
    emojis = {
        'rock': '🪨',
        'paper': '📄',
        'scissors': '✂️'
    }
    
    print(f"\n{'='*40}")
    print(f"You chose:     {emojis[user_choice]} {user_choice.capitalize()}")
    print(f"Computer chose: {emojis[computer_choice]} {computer_choice.capitalize()}")
    print(f"{'='*40}")
    
    if result == "win":
        print("🎉 You win! Great job!")
    elif result == "lose":
        print("🤖 Computer wins! Better luck next time!")
    else:
        print("🤝 It's a tie!")

def play_game():
    """Main game loop."""
    print("\n🎮 Welcome to Rock Paper Scissors! 🎮")
    print("Rules: rock beats scissors, scissors beats paper, paper beats rock\n")
    
    score = {"wins": 0, "losses": 0, "ties": 0}
    
    while True:
        user_input = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower().strip()
        
        if user_input == 'quit':
            print(f"\n📊 Final Score: {score['wins']} wins, {score['losses']} losses, {score['ties']} ties")
            print("Thanks for playing! 👋\n")
            break
        
        if user_input not in ['rock', 'paper', 'scissors']:
            print("❌ Invalid choice! Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        result = determine_winner(user_input, computer_choice)
        display_result(user_input, computer_choice, result)
        
        if result == "win":
            score["wins"] += 1
        elif result == "lose":
            score["losses"] += 1
        else:
            score["ties"] += 1
        
        print(f"Score: {score['wins']}W - {score['losses']}L - {score['ties']}T")

if __name__ == "__main__":
    play_game()