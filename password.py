import random
import streamlit as st

st.title("Password Generator")
st.write("Generate a secure password")

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0123456789"
symbols="!@#$%&()_."

all=lower + upper + digits + symbols

length = st.slider("Select password length", min_value=8, max_value=32, value=16)
if st.button("Generate Password"):
    password = "".join(random.sample(all, length))
    st.write("Your generated password is:")
    st.code(password)