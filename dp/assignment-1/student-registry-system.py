print("Welcome to DPLMS Student Register System")

courses = ["Python with AI/ML", "JavaScript", "Flutter", "MERN Stack"];

print("Available Courses are: ")

for i in courses: 
    print(i);

name = input('Enter your name: ');
email = input("Enter your email: ");
age = input("Enter your age: ")
selected_course = input("Enter the selected course name: ");

if(selected_course in courses): 
    print("Registration Successful!")
    print(f"Hi, {name}, you have successfully enrolled in the {selected_course} Course.");
else : 
    print("Course not available!");


