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

st.title("☕ Java Basics")

st.header("Variables")

st.code("""
public class Main {
    public static void main(String[] args) {
        String name = "Ashish";
        int age = 20;

        System.out.println(name);
        System.out.println(age);
    }
}
""", language="java")

st.header("Data Types")

st.code("""
String name = "Ashish";
int age = 20;
double height = 5.8;
char grade = 'A';
boolean isStudent = true;
""", language="java")

st.header("Input and Output")

st.code("""
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Name: ");
        String name = sc.nextLine();

        System.out.println("Hello " + name);
    }
}
""", language="java")

st.header("Operators")

st.code("""
int a = 10;
int b = 5;

System.out.println(a + b);
System.out.println(a - b);
System.out.println(a * b);
System.out.println(a / b);
""", language="java")

st.header("If Else")

st.code("""
int age = 20;

if(age >= 18) {
    System.out.println("Adult");
}
else {
    System.out.println("Minor");
}
""", language="java")

st.header("Switch Case")

st.code("""
int day = 2;

switch(day) {
    case 1:
        System.out.println("Monday");
        break;

    case 2:
        System.out.println("Tuesday");
        break;

    default:
        System.out.println("Invalid");
}
""", language="java")

st.header("For Loop")

st.code("""
for(int i = 1; i <= 5; i++) {
    System.out.println(i);
}
""", language="java")

st.header("While Loop")

st.code("""
int i = 1;

while(i <= 5) {
    System.out.println(i);
    i++;
}
""", language="java")

st.header("Methods")

st.code("""
public class Main {

    static void greet() {
        System.out.println("Hello Ashish");
    }

    public static void main(String[] args) {
        greet();
    }
}
""", language="java")

st.header("Method with Parameters")

st.code("""
public class Main {

    static void greet(String name) {
        System.out.println("Hello " + name);
    }

    public static void main(String[] args) {
        greet("Ashish");
    }
}
""", language="java")

st.header("Arrays")

st.code("""
String[] names = {
    "Ashish",
    "Rahul",
    "Amit"
};

for(String name : names) {
    System.out.println(name);
}
""", language="java")

st.header("Strings")

st.code("""
String name = "Ashish";

System.out.println(name.length());
System.out.println(name.charAt(0));
""", language="java")

st.header("Classes and Objects")

st.code("""
class Student {
    String name;

    void display() {
        System.out.println(name);
    }
}

public class Main {
    public static void main(String[] args) {
        Student s1 = new Student();

        s1.name = "Ashish";
        s1.display();
    }
}
""", language="java")

st.header("Constructors")

st.code("""
class Student {
    String name;

    Student(String name) {
        this.name = name;
    }
}

public class Main {
    public static void main(String[] args) {
        Student s1 = new Student("Ashish");
    }
}
""", language="java")

st.header("Inheritance")

st.code("""
class Person {
    void show() {
        System.out.println("Person Class");
    }
}

class Student extends Person {
}

public class Main {
    public static void main(String[] args) {
        Student s1 = new Student();
        s1.show();
    }
}
""", language="java")

st.header("ArrayList")

st.code("""
import java.util.ArrayList;

ArrayList<String> names = new ArrayList<>();

names.add("Ashish");
names.add("Rahul");
names.add("Amit");

for(String name : names) {
    System.out.println(name);
}
""", language="java")

st.success("Java Basics Completed 🚀")