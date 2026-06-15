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

st.logo("CODE_HELPER_LOGO.png")

st.title("💻 CODE HELPER")
st.caption("Your Quick Programming Syntax Companion")

st.info(
    """
    Code Helper is designed for students, beginners, and professionals
    who need instant access to programming syntax, examples, and coding references.
    Learn faster, code smarter, and save time.
    """
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric("Multiple Languages","3")

with col2:
    st.metric("Code Examples","30+")

st.divider()

st.subheader("🚀 Why Use Code Helper?")

c1, c2 = st.columns(2)

with c1:
    st.success("⚡ Quick access to programming syntax")
    st.success("📚 Beginner-friendly examples")
    st.success("🎯 Useful for assignments and projects")

with c2:
    st.success("💼 Helpful for professionals")
    st.success("🔍 Easy to navigate")
    st.success("⏱️ Saves time and boosts productivity")

st.divider()

st.header("✨ Key Features")

feature1, feature2, feature3 = st.columns(3)

with feature1:
    st.markdown("### 🐍 Python")
    st.write(
        """
        Learn Python syntax including:
        - Variables
        - Loops
        - Functions
        - Lists
        - Dictionaries
        """
    )

with feature2:
    st.markdown("### ☕ Java")
    st.write(
        """
        Learn Java concepts including:
        - Classes
        - Objects
        - Methods
        - Arrays
        - Inheritance
        """
    )

with feature3:
    st.markdown("### ⚙️ C++")
    st.write(
        """
        Learn C++ topics including:
        - Variables
        - Loops
        - Functions
        - Pointers
        - OOP Concepts
        """
    )

st.divider()

st.success("🎉 Start Learning and Coding with Code Helper!")








# st.logo("CODE_HELPER_LOGO.png")

# st.markdown(
#     """
#     <h1 style="font-size:80px;">
#         CODE HELPER
#     </h1>
#     """,
#     unsafe_allow_html=True
# )

# st.markdown("""
# **Code Helper is a simple and efficient application designed for students, beginners, and working professionals who need instant access to programming syntax and code references. Instead of searching through lengthy documentation, users can quickly find the basic syntax, examples, and usage of various programming languages in one place.
# Whether you are learning to code, preparing for interviews, working on assignments, or developing real-world projects, Code Helper serves as a handy reference tool to boost productivity and reduce coding errors. The app provides clear, organized, and easy-to-understand syntax examples for popular programming languages and technologies.**
# """)    

# st.markdown("""
# <h1 style="font-size:40px;">
# Key Features
# </h1>
# """, unsafe_allow_html=True)

# st.markdown("""
# - Quick access to basic programming syntax
# - Beginner-friendly explanations and examples
# - Supports multiple programming languages
# - Easy navigation and clean interface
# - Useful for students, developers, and professionals
# - Saves time by providing instant code references
# """)
