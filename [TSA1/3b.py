# Initialize the row counter
i = 1

# Loop through each row
while i <= 7:
    # Print spaces for alignment
    j = 1
    while j <= (7 - i) // 2:
        print(" ", end="")  # Print space without a newline
        j += 1  # Increment the space counter

    # Print the number i, i times
    k = 1
    while k <= i:
        print(i, end="")  # Print the number without a newline
        k += 1  # Increment the number counter

    # Move to the next line after each row
    print()  # Print a newline

    # Increment the row counter by 2 for the next odd number
    i += 2