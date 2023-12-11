# Imagine working on software that processes text. A palindrome is a word,
# phrase, or sequence that reads the same backward as forward.

# Create a function named palindrome that determines if a string is a palindrome.
# This method should take in one string as a parameter. This method should return
# True if the string is a palindrome.

# Examples
# Original string as parameter        Is it a palindrome?
# "Hello, world!"                     No
# "racecar"                           Yes
# "noon"                              Yes
# "mom"                               Yes
# "kayak"                             Yes

# When considering example inputs and outputs, you likely considered edge cases.
# Your solution is only required to handle the nominal cases. As time allows,
# consider how to handle the edge cases you identified.

def palindrome(input_string):
    # Clean the input string: convert to lowercase and only keep alphabetic characters
    cleaned_string = ''.join(character.lower() for character in input_string if character.isalpha())
    
    # Reverse the cleaned string using slicing
    reversed_cleaned_string = cleaned_string[::-1]

    # Check if the cleaned string and the reversed cleaned string are equal
    return cleaned_string == reversed_cleaned_string
    print(palindrome(mom))

# The time complexity is O(n), where n is the input string's length. 
# It spends O(n) time cleaning and joining characters, O(n) time reversing 
# the cleaned string, and O(n) time comparing the cleaned and reversed strings.

# The space complexity is O(n), where n is the length of the input string. 
# This is because it creates a cleaned string and a reversed cleaned string,
# both of which can have a maximum length of n. The space needed for these strings 
# is proportional to the input string's length, resulting in a linear O(n) space complexity. 

def palindrome(input_string):
    # Clean the input string: convert to lowercase and remove non-alphabetic characters
    cleaned_string = ''.join(character.lower() for character in input_string if character.isalpha())
    
    # Reverse the cleaned string using slicing
    reversed_cleaned_string = cleaned_string[::-1]

    # Check if the cleaned string and the reversed cleaned string are equal
    return cleaned_string == reversed_cleaned_string

# Example usage of the palindrome function
example_string = "mom"
print(palindrome(example_string))  # Output: True
