import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

test = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", test)
st.title(f"A Movie of {test}")  # Using f-string for string interpolation
