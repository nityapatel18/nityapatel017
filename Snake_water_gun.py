import random
import streamlit as st

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

# Streamlit App
def main():
    st.title("🐍💧🔫 Snake, Water, Gun Game")

    # Player choice via radio button
    player_choice = st.radio("Choose your option:", ['snake', 'water', 'gun'])

    if st.button("Play"):
        computer_choice = random.choice(['snake', 'water', 'gun'])
        result = check(player_choice, computer_choice)
        st.write(f"You chose **{player_choice}**, computer chose **{computer_choice}**.")
        st.success(result)

if __name__ == "__main__":
    main()

