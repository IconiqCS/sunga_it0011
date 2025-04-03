# Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenate first and last name
full_name = first_name + " " + last_name

# Convert to uppercase and lowercase
upper_name = full_name.upper()
lower_name = full_name.lower()

# Get the length of the full name
name_length = len(full_name)

# Display results
print("\nFull Name:", full_name)
print("Full Name (Upper Case):", upper_name)
print("Full Name (Lower Case):", lower_name)
print("Length of Full Name:", name_length)
