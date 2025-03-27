# Function to perform division
def divide(num1, num2):
    if num2 == 0:  # Check if the denominator is zero
        print("Error: Cannot divide by zero.")
        return None
    return num1 / num2

# Function to perform exponentiation
def exponentiate(base, exponent):
    return base ** exponent  # Return base raised to the power of exponent

# Function to perform remainder operation
def remainder(num1, num2):
    if num2 == 0:  # Check if the denominator is zero
        print("Error: Cannot divide by zero.")
        return None
    return num1 % num2

# Function to perform summation
def summation(start, end):
    if start > end:  # Check if the second number is greater than the first
        print("Error: The second number must be greater than the first.")
        return None
    total = 0
    for num in range(start, end + 1):  # Sum from start to end
        total += num
    return total

# Function to display the menu and get user choice
def display_menu():
    print("Choose an operation:")
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")
    print("[Q] - Quit")

# Main function to run the program
def main():
    while True:
        display_menu()  # Show the menu
        choice = input("Enter your choice: ").upper()  # Get user choice and convert to uppercase

        if choice == 'Q':  # Quit the program
            print("Exiting the program.")
            break

        if choice == 'D':  # Division
            num1 = float(input("Enter the numerator: "))
            num2 = float(input("Enter the denominator: "))
            result = divide(num1, num2)
            if result is not None:
                print(f"Result: {result}")

        elif choice == 'E':  # Exponentiation
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            result = exponentiate(base, exponent)
            print(f"Result: {result}")

        elif choice == 'R':  # Remainder
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = remainder(num1, num2)
            if result is not None:
                print(f"Result: {result}")

        elif choice == 'F':  # Summation
            start = int(input("Enter the first number (limit): "))
            end = int(input("Enter the second number (limit): "))
            result = summation(start, end)
            if result is not None:
                print(f"Result: {result}")

        else:
            print("Invalid choice! Please try again.")  # Handle invalid input

# Run the main function
if __name__ == "__main__":
    main()  # Start the program