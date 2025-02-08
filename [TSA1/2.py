# Initialize the sum variable
sum_of_digits = 0

# Get input from the user
input_string = input("Enter a string containing digits: ")

# Loop through each character in the input string
for char in input_string:
    # Check if the character is a digit
    if char.isdigit():
        # Convert the character to an integer and add it to the sum
        sum_of_digits += int(char)

# Print the result
print("The sum of the digits is:", sum_of_digits)