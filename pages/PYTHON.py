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
        background-attachment: scroll;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🐍 Python Basics Examples")

st.write("Welcome! Learn the basics of Python with simple examples.")

st.header("Variables")

st.code("""
name = "Ashish"
age = 20

print(name)
print(age)
""", language="python")

st.write("Variables are used to store data.")

st.header("Data Types")

st.code("""
name = "Ashish"     # String
age = 21            # Integer
height = 5.7        # Float
is_student = True   # Boolean
""", language="python")

st.write("Python has different data types such as String, Integer, Float, and Boolean.")

st.header("User Input")

st.code("""user_name = st.text_input("Enter your name:")

if user_name:
    st.success(f"Hello, {user_name}!")""")

st.header("If-Else Statements")

st.code("""
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
""", language="python")

st.header("Loops")

st.code("""
for i in range(5):
    print(i)
""", language="python")

st.write("Output:")
for i in range(5):
    st.write(i)

st.header("Functions")

st.code("""
def greet(name):
    return f"Hello, {name}"

print(greet("Ashish"))
""", language="python")

st.header("Lists")

st.code("""
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
""", language="python")

fruits = ["Apple", "Banana", "Mango"]
st.write("List Example:", fruits)

st.header(" Dictionary")

st.code("""
student = {
    "name": "Ashish",
    "age": 20
}

print(student["name"])
""", language="python")

st.header(" Python Basics Covered")

st.success("Java Basics Completed 🚀")