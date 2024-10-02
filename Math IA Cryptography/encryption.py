import math

# Define the letter-to-number dictionary
letter_to_number = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
    'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
    'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
    'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

# Create a reverse mapping from numbers back to letters
number_to_letter = {v: k for k, v in letter_to_number.items()}

# Take user input, convert to uppercase
user_input = input("Enter a word: ").upper()

# Convert the input letters to numbers using the dictionary
converted_numbers = [letter_to_number[letter] for letter in user_input if letter in letter_to_number]

# Calculate e^x for each converted number and then modulus 26
exp_mod_values = [int(math.exp(x) % 26) for x in converted_numbers]

# Convert the mod values back to letters, using 26 to represent 'Z'
resulting_letters = [number_to_letter[num] if num != 0 else 'Z' for num in exp_mod_values]

print(f"Converted numbers: {converted_numbers}")
print(f"e^x mod 26 values: {exp_mod_values}")
print(f"Resulting letters: {resulting_letters}")
