import random

# Function to check winner
def check(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == 'snake' and computer_choice == 'water') or
        (player_choice == 'water' and computer_choice == 'gun') or
        (player_choice == 'gun' and computer_choice == 'snake')
    ):
        return "You win!"
    else:
        return "Computer wins!" 

# Main game
def main():
    print("🐍💧🔫 Welcome to Snake, Water, Gun game!")
    player_choice = input("Enter your choice (snake, water, gun): ").lower()
    computer_choice = random.choice(['snake', 'water', 'gun'])
    result = check(player_choice, computer_choice)
    print(f"You chose {player_choice}, computer chose {computer_choice}. {result}")

if __name__ == "__main__":
    main()
