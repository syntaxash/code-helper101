import streamlit as st
import base64

def get_base64(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("background.jpg")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔐 SIGN IN")
st.write("Welcome back! Sign in to continue.")
    
email = st.text_input("📧 Email")
password = st.text_input("🔑 Password", type="password")
    
st.divider()

col1, col2,col3 = st.columns([1,1,1])

with col1:
        if st.button("*Create Account*", use_container_width=True):
            st.info("Redirecting to Sign Up...")
    
with col2:
        if st.button("*Sign in*", use_container_width=True):
            st.success("You are signed up!")

with col3:
        if st.button("*Forgot Password*", use_container_width=True):
            st.info("Redirecting to Password Recovery...")