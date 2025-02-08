# Get input from the user
input_string = input("Enter a string: ")

# Initialize counters
vowel_count = 0
consonant_count = 0
space_count = 0
other_count = 0

# Define vowels
vowels = "aeiouAEIOU"

# Loop through each character in the input string
for char in input_string:
    if char.isalpha():  # Check if the character is a letter
        if char in vowels:  # Check if the character is a vowel
            vowel_count += 1
        else:  # If it's a letter but not a vowel, it's a consonant
            consonant_count += 1
    elif char.isspace():  # Check if the character is a space
        space_count += 1
    else:  # If it's neither a letter nor a space, it's another character
        other_count += 1

# Display the results
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
print("Number of spaces:", space_count)
print("Number of other characters:", other_count)