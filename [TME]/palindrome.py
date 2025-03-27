#it sets the file path to the location of the numbers.txt file
file_path = "C:/Users/Charles/Downloads/numbers.txt"

#this will open and process the file
with open(file_path, "r") as file:
    # Read all lines from file
    lines = file.readlines()

    #it will process each line
    line_number = 1
    for line in lines:
        #i remove spaces and used comma to split the numbers.
        numbers = line.strip().split(',')

        #it will calculate sum of numbers
        total = 0
        for num in numbers:
            total = total + int(num)

        #convert sum to string to check palindrome
        sum_str = str(total)

        #checks if sum is palindrome
        if sum_str == sum_str[::-1]:
            result = "Palindrome"
        else:
            result = "Not a palindrome"

        #print the output
        print ("----------------------------------------------------------")
        print(f"Line {line_number}: {line.strip()} (sum {total}) - {result}")
        print ("----------------------------------------------------------")
        #will increment line number
        line_number = line_number + 1