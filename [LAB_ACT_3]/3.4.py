# Opening the file in read mode
try:
    with open("students.txt", "r") as file:
        # Reading the contents of the file
        content = file.readlines()

        # Displaying the student information
        print("Reading Student Information:")
        for line in content:
            print(line.strip())  # Using strip() to remove any leading/trailing whitespace

except FileNotFoundError:
    print("The file 'students.txt' was not found. Please make sure it exists.")
except Exception as e:
    print(f"An error occurred: {e}")