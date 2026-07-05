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
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
if st.session_state.get("email",False):
    st.write("You are safely inside the app!")
else:
    st.warning("login!!!")
    st.stop()


st.logo("CODE_HELPER_LOGO.png")


col1, col2 = st.columns([4, 1])

with col1:
    st.success(f"Welcome: {st.session_state['email']}")
    
with col2:
    if st.button("🚪 Logout", use_container_width=True):

     del st.session_state["email"]
     st.switch_page("pages/SIGN_IN.py") #indentaion error was here



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


m1, m2 = st.columns(2)

with m1:
    st.metric("Multiple Languages", "3")

with m2:
    st.metric("Code Examples", "30+")

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



st.header("✨ Choose a Language")

feature1, feature2, feature3 = st.columns(3)

with feature1:
    st.markdown("### 🐍 Python")
    st.write("""
    - Variables
    - Loops
    - Functions
    - Lists
    - Dictionaries
    """)

    if st.button("Open Python", use_container_width=True):
        st.switch_page("pages/Python.py")

with feature2:
    st.markdown("### ☕ Java")
    st.write("""
    - Classes
    - Objects
    - Methods
    - Arrays
    - Inheritance
    """)

    if st.button("Open Java", use_container_width=True):
        st.switch_page("pages/Java.py")

with feature3:
    st.markdown("### ⚙️ C++")
    st.write("""
    - Variables
    - Loops
    - Functions
    - Pointers
    - OOP Concepts
    """)

    if st.button("Open C++", use_container_width=True):
        st.switch_page("pages/Cpp.py")

st.divider()

st.success("🎉 Start Learning and Coding with Code Helper!")

