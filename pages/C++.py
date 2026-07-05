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
if st.session_state.get("email",False):
    st.write("You are safely inside the app!")
else:
    st.warning("login!!!")
    st.stop()

st.title("⚙️ C++ Basics")

st.header("Variables")

st.code("""
#include <iostream>
using namespace std;

int main() {
    string name = "Ashish";
    int age = 20;

    cout << name << endl;
    cout << age << endl;

    return 0;
}
""", language="cpp")

st.header("Data Types")

st.code("""
string name = "Ashish";
int age = 20;
float height = 5.8;
char grade = 'A';
bool isStudent = true;
""", language="cpp")

st.header("Input and Output")

st.code("""
#include <iostream>
using namespace std;

int main() {
    string name;

    cout << "Enter Name: ";
    cin >> name;

    cout << "Hello " << name;

    return 0;
}
""", language="cpp")

st.header("Operators")

st.code("""
int a = 10;
int b = 5;

cout << a + b << endl;
cout << a - b << endl;
cout << a * b << endl;
cout << a / b << endl;
""", language="cpp")

st.header("If Else")

st.code("""
int age = 20;

if(age >= 18) {
    cout << "Adult";
}
else {
    cout << "Minor";
}
""", language="cpp")

st.header("Switch Case")

st.code("""
int day = 2;

switch(day) {
    case 1:
        cout << "Monday";
        break;

    case 2:
        cout << "Tuesday";
        break;

    default:
        cout << "Invalid";
}
""", language="cpp")

st.header("For Loop")

st.code("""
for(int i = 1; i <= 5; i++) {
    cout << i << endl;
}
""", language="cpp")

st.header("While Loop")

st.code("""
int i = 1;

while(i <= 5) {
    cout << i << endl;
    i++;
}
""", language="cpp")

st.header("Functions")

st.code("""
#include <iostream>
using namespace std;

void greet() {
    cout << "Hello Ashish";
}

int main() {
    greet();
    return 0;
}
""", language="cpp")

st.header("Function with Parameters")

st.code("""
#include <iostream>
using namespace std;

void greet(string name) {
    cout << "Hello " << name;
}

int main() {
    greet("Ashish");
    return 0;
}
""", language="cpp")

st.header("Arrays")

st.code("""
string names[3] = {"Ashish", "Rahul", "Amit"};

for(int i = 0; i < 3; i++) {
    cout << names[i] << endl;
}
""", language="cpp")

st.header("Strings")

st.code("""
string name = "Ashish";

cout << name.length() << endl;
cout << name[0] << endl;
""", language="cpp")

st.header("Structures")

st.code("""
struct Student {
    string name;
    int age;
};

Student s1;
s1.name = "Ashish";
s1.age = 20;

cout << s1.name;
""", language="cpp")

st.header("Pointers")

st.code("""
int num = 10;
int *ptr = &num;

cout << *ptr;
""", language="cpp")

st.header("Classes and Objects")

st.code("""
#include <iostream>
using namespace std;

class Student {
public:
    string name;

    void display() {
        cout << name;
    }
};

int main() {
    Student s1;
    s1.name = "Ashish";
    s1.display();

    return 0;
}
""", language="cpp")

st.header("Vectors")

st.code("""
#include <vector>

vector<string> names = {
    "Ashish",
    "Rahul",
    "Amit"
};

for(string name : names) {
    cout << name << endl;
}
""", language="cpp")

st.success("C++ Basics Completed 🚀")