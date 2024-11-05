import streamlit as st

# Set the title of the app
st.title("Simple Streamlit App")

# Create a text input for the user's name
name = st.text_input("Enter your name:")

# Create a button to submit the name
if st.button("Submit"):
    if name:
        st.success(f"Hello, {name}! Welcome to the Streamlit app.")
    else:
        st.warning("Please enter your name.")
