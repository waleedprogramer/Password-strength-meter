import streamlit as st
from zxcvbn import zxcvbn
import secrets
import string

def check_password_strength(password):
    """Check the strength of a password using zxcvbn."""
    strength = zxcvbn(password)
    score = strength['score']
    feedback = strength['feedback']['suggestions']

    strength_labels = ["Very Weak 🔴", "Weak 🟠", "Medium 🟡", "Strong 🟢", "Very Strong 🔵"]
    return strength_labels[score], feedback

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """Generates a secure random password based on user preferences."""
    character_pool = ""

    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        return "Error: No character type selected."

    password = ''.join(secrets.choice(character_pool) for _ in range(length))
    return password

st.title("🔐 Password Strength Meter & Generator")
menu = st.sidebar.radio("🔍 Navigation", ["Check Your Password Strength", "Password Generator"])
st.sidebar.info("🔐 Use this tool to check your password strength & generate a strong password!")

if menu == "Check Your Password Strength":
  password = st.text_input("Enter your password:", type="password")
  if password:
    strength, feedback = check_password_strength(password)
    st.subheader(f"Password Strength: {strength}")

    if feedback:
        st.write("Suggestions to improve your password:")
        for tip in feedback:
            st.write(f"- {tip}")
elif menu == "Password Generator":
  st.subheader("🔑 Generate a Secure Password")
  length = st.slider("Password Length:", min_value=8, max_value=32, value=12)
  use_upper = st.checkbox("Include Uppercase Letters", value=True)
  use_lower = st.checkbox("Include Lowercase Letters", value=True)
  use_digits = st.checkbox("Include Digits", value=True)
  use_symbols = st.checkbox("Include Symbols", value=True)

  if st.button("⚡ Generate Password"):
    new_password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    st.success("✅ Password Generated Successfully!")
    editable_password = st.text_input("✍️ Edit or Copy Password:", value=new_password)
    st.write("_Modify if needed, then copy and use this strong password!_")
