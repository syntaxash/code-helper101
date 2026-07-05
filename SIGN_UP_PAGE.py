import streamlit as st
import base64

import pymongo
conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")

mydb=conn["users"]#users is database on mongodb
my=mydb["user_info"]#user_info is a collection on mongodb

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
        background-attachment: scroll;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.image("logo1.png",width=200)
with col2:
    st.image("logo2.png",width=200)
with col3:
    st.image("logo3.png",width=200)
st.title("💻S I G N   U P")
t1=st.text_input("🌐*ADD EMAIL*")
t2=st.text_input("🔐*ENTER YOUR PASSWORD*",type="password")
t3=st.text_input("📞*MOBILE NO.*")
t4=st.text_input("🪪*ENTER YOUR USERNAME*")
t5=st.date_input("📆*ENTER YOUR DOB*")
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("*Sign in*", use_container_width=True):
        st.info("Ready to sign in!")
        st.switch_page("pages/SIGN_IN.py")
     
with col2:

    if st.button("*Sign up*", use_container_width=True):
       
       my.insert_one({"email":t1,"password":t2,"mobile":str(t3),"username":t4,"dob":str(t5)})

       st.success("Signed Up Successfully!")
       st.balloons()

with col3:
    if st.button("*Forgot password*", use_container_width=True):
        st.info("Changing password!")
        
