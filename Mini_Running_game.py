import streamlit as st
import time
import random

# Game state
if "score" not in st.session_state:
    st.session_state.score = 0
if "player_y" not in st.session_state:
    st.session_state.player_y = 0
if "obstacles" not in st.session_state:
    st.session_state.obstacles = []

st.title("🚇 Mini Subway Surfers Demo")

# Jump button
if st.button("Jump"):
    st.session_state.player_y = 1  # jump

# Gravity effect
if st.session_state.player_y > 0:
    st.session_state.player_y -= 0.2
    if st.session_state.player_y < 0:
        st.session_state.player_y = 0

# Add new obstacle randomly
if random.random() < 0.1:
    st.session_state.obstacles.append(10)

# Move obstacles
new_obstacles = []
for obs in st.session_state.obstacles:
    obs -= 1
    if obs > 0:
        new_obstacles.append(obs)
st.session_state.obstacles = new_obstacles

# Collision check
game_over = False
for obs in st.session_state.obstacles:
    if obs == 1 and st.session_state.player_y == 0:
        game_over = True

# Draw game
canvas = ["⬜"] * 12
canvas[1] = "🟦" if st.session_state.player_y == 0 else "🔵"
for obs in st.session_state.obstacles:
    if obs < len(canvas):
        canvas[obs] = "⬛"

st.write("".join(canvas))

if game_over:
    st.error("💥 Game Over!")
    st.session
