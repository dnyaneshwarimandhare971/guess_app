import streamlit as st
import random

st.title("🐍 Number Guessing App")

# Initialize secret number in "session state" so it doesn't change every click
if 'target' not in st.session_state:
    st.session_state.target = random.randint(1, 100)

guess = st.number_input("Enter your guess:", min_value=1, max_value=100)

if st.button("Submit Guess"):
    if guess < st.session_state.target:
        st.warning("Too low!")
    elif guess > st.session_state.target:
        st.warning("Too high!")
    else:
        st.success(f"You got it! The number was {st.session_state.target}")
        if st.button("Play Again"):
            del st.session_state.target
            st.rerun()