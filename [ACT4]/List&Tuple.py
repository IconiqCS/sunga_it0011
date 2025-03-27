import json  # Importing the json module to handle file operations

students = []  # List to store student records

def add_student():
    """Function to add a student record"""
    student_id = input("Enter Student ID (6 digits): ")  # Validate that the student ID is a 6-digit number
    while not (student_id.isdigit() and len(student_id) == 6):
        print("Invalid ID! Must be a 6-digit number.")
        student_id = input("Enter Student ID (6 digits): ")

    # Get the student's first and last name
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    full_name = (first_name, last_name)  # Store as a tuple

    # Get the student's class standing and major exam grades
    class_standing = float(input("Enter Class Standing Grade: "))
    major_exam = float(input("Enter Major Exam Grade: "))

    # Create a student record as a tuple and add it to the students list
    student = (student_id, full_name, class_standing, major_exam)
    students.append(student)
    print("Student record added successfully!\n")

def display_students():
    """Function to display all student records"""
    if not students:
        print("No student records found!\n")
        return

    print("\nStudent Records:")
    # Loop through each student and print their details
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1][0]} {student[1][1]}, Class Standing: {student[2]}, Major Exam: {student[3]}")
    print("\n")

def save_file(filename="students.json"):
    """Function to save student records to a file"""
    with open(filename, "w") as file:
        json.dump(students, file)  # Write the students list to the file in JSON format
    print("Records saved successfully!\n")

def open_file(filename="students.json"):
    """Function to load student records from a file"""
    local_students = []  # Temporary list to hold loaded students
    try:
        with open(filename, "r") as file:
            local_students = json.load(file)  # Load records from the file
        students.clear()  # Clear the current students list
        students.extend(local_students)  # Add loaded records to the students list
        print("Records loaded successfully!\n")
    except FileNotFoundError:
        print("File not found!\n")  # Handle case where the file does not exist

def order_by_last_name():
    """Function to order students by their last name"""
    sorted_students = sorted(students, key=lambda x: x[1][1])  # Sort by last name
    print("\nStudents Ordered by Last Name:")
    for student in sorted_students:
        print(f"ID: {student[0]}, Name: {student[1][0]} {student[1][1]}, Class Standing: {student[2]}, Major Exam: {student[3]}")
    print("\n")

def order_by_grade():
    """Function to order students by their final grade"""
    sorted_students = sorted(students, key=lambda x: (x[2] * 0.6 + x[3] * 0.4), reverse=True)  # Sort by final grade
    print("\nStudents Ordered by Grade:")
    for student in sorted_students:
        final_grade = student[2] * 0.6 + student[3] * 0.4  # Calculate final grade
        print(f"ID: {student[0]}, Name: {student[1][0]} {student[1][1]}, Final Grade: {final_grade:.2f}")
    print("\n")

def show_student_record():
    """Function to show a specific student record by ID"""
    student_id = input("Enter Student ID to search: ")
    for student in students:
        if student[0] == student_id:  # Check if the ID matches
            print(f"ID: {student[0]}, Name: {student[1][0]} {student[1][1]}, Class Standing: {student[2]}, Major Exam: {student[3]}")
            return
    print("Student not found!\n")  # Handle case where student ID is not found

def edit_record():
    """Function to edit an existing student record"""
    student_id = input("Enter Student ID to edit: ")
    for i, student in enumerate(students):
        if student[0] == student_id: # Get new values for the record
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            class_standing = float(input("Enter Class Standing Grade: "))
            major_exam = float(input("Enter Major Exam Grade: "))

            # Update the student record with new values
            students[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("Record updated successfully!\n")
            return
    print("Student not found!\n")  # Handle case where student ID is not found

def delete_record():
    """Function to delete a student record by ID"""
    student_id = input("Enter Student ID to delete: ")
    global students
    students = [student for student in students if student[0] != student_id]  # Filter out the student with the given ID
    print("Record deleted successfully!\n")

def main():
    """Main function to run the student record management system"""
    while True:
        # Display the menu options
        print("=====================================")
        print("STUDENT RECORD MANAGEMENT SYSTEM")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        print("=====================================")

        choice = input("Enter your choice: ")  # Get user choice
        if choice == "1":
            open_file()  # Open file to load records
        elif choice == "2":
            save_file()  # Save records to the default file
        elif choice == "3":
            filename = input("Enter filename: ")  # Get new filename for saving
            save_file(filename)  # Save records to the specified file
        elif choice == "4":
            display_students()  # Show all student records
        elif choice == "5":
            order_by_last_name()  # Order records by last name
        elif choice == "6":
            order_by_grade()  # Order records by final grade
        elif choice == "7":
            show_student_record()  # Show a specific student record
        elif choice == "8":
            add_student()  # Add a new student record
        elif choice == "9":
            edit_record()  # Edit an existing student record
        elif choice == "10":
            delete_record()  # Delete a student record
        elif choice == "11":
            print("Exiting program...")  # Exit the program
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 11.\n")

if __name__ == "__main__":
    main()  # Start the program