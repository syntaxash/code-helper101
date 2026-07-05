import streamlit as st
import base64

import pymongo
conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
mydb=conn["users"]
my=mydb["user_info"]


valid = 0
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
    
email = st.text_input("📧 email")
password = st.text_input("🔑 Password", type="password")
    
st.divider()

col1, col2,col3 = st.columns([1,1,1])

with col1:
        if st.button("*Create Account*", use_container_width=True):
            st.info("Redirecting to Sign Up...")
            st.switch_page("SIGN_UP_PAGE.py")

with col2:
        valid=0
        if st.button("*Sign in*", use_container_width=True):
         ans=my.find({"email":email,"password":password})
         for i in ans:
              valid=valid+1
              st.session_state["email"]=i['email']
              st.session_state["password"]=i['password']
              st.switch_page("pages/APP.py")
                             
        if valid==0:
              st.success("Invalid User Login Details")




with col3:
        if st.button("*Forgot Password*", use_container_width=True):
            st.info("Redirecting to Password Recovery...")