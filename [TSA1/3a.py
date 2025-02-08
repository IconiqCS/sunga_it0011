# Number of rows for the pattern
rows = 5

# Loop through each row
for i in range(1, rows + 1):
    # Print spaces for alignment
    for j in range(rows - i):
        print(" ", end="")  # Print space without a newline

    # Print numbers from 1 to i
    for k in range(1, i + 1):
        print(k, end="")  # Print number without a newline

    # Move to the next line after each row
    print()  # Print a newline