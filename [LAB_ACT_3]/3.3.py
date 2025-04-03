# Get user input
last_name = input("Enter last name: ")
first_name = input("Enter first name: ")
age = input("Enter age: ")
contact_number = input("Enter contact number: ")
course = input("Enter course: ")

# Format the collected information
student_info = f"Last Name: {last_name}\nFirst Name: {first_name}\nAge: {age}\nContact Number: {contact_number}\nCourse: {course}\n\n"

# Open the file in append mode and write the information
with open("students.txt", "a") as file:
    file.write(student_info)

# Display confirmation message
print("Student information has been saved to 'students.txt'.")
