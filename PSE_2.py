# Imagine programming the logic for a word game.
# In this game, every player submits one word. Each word gets a score based on
# the letters in the word and its point value.
# Create a function named score that is responsible for scoring a given word.
# This function should take in a string named word as a parameter. This function
# should return the word's total number of points.
# Refer to this table for the point values of each letter.
#
# Letter Value:
# A, E, I, O, U, L, N, R, S, T - 1
# D, G - 2
# B, C, M, P - 3
# F, H, V, W, Y - 4
# K - 5
# J, X - 8
# Q, Z - 10

#example 
# Examples:
# Input       Expected Output
# "DOG"       5
# "CAT"       5
# "CABBAGE"   14
# "QUARTZ"    24
# ""          0
# "Dog"       5
# "DOG"       5
# "dOG"       5
# "dOG!@)"    5


def score(word):
    letter_values = {
    "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
    "D": 2, "G": 2,
    "B": 3, "C": 3, "M": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
    "K": 5,
    "J": 8, "X": 8,
    "Q": 10, "Z": 10
}
    total_score = 0
    for letter in word.upper():
        total_score += letter_values.get(letter, 0)
    return total_score


# Use a Dictionary Comprehension for Case-Insensitive Matching: Instead of 
# calling .upper() on every letter in the word, you can prepare your 
# letter_values dictionary to handle both uppercase and lowercase letters. This 
# way, you can look up the score for each letter directly without needing to 
# convert it.

# Use sum with a Generator Expression: This is more of a stylistic choice. 
# Instead of manually initializing and updating total_score, you can use 
# Python's sum function with a generator expression for a more concise and 
# Pythonic approach.


def score(word):
    letter_values = {
        **{letter: 1 for letter in "AEIOULNRST"},
        **{letter: 2 for letter in "DG"},
        **{letter: 3 for letter in "BCMP"},
        **{letter: 4 for letter in "FHVWY"},
        **{letter: 5 for letter in "K"},
        **{letter: 8 for letter in "JX"},
        **{letter: 10 for letter in "QZ"}
    }

    # Add lowercase keys as well
    letter_values.update({k.lower(): v for k, v in letter_values.items()})

    return sum(letter_values.get(letter, 0) for letter in word)

# Example usage
print(score("CABBAGE"))  # Output: 14

