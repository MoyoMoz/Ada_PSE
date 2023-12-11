# Imagine working on software that analyzes mutations in DNA.
#
# Create a function named hamming_distance that calculates the number of
# differences between two DNA strands (aka two strings). This method should
# take in two different DNA strands of the same length as parameters. This
# method should have a return value of the number of differences between each
# string.
#
# For example, given these two DNA strands (strings), hamming_distance should
# return 7 because there are 7 differences:
#
# Example Input         Expected Output
# strand1 = "GAGCCTACTAACGGGAT"
# strand2 = "CATCGTAATGACGGCCT"    7
# strand1 = "GAG"
# strand2 = "GAG"                 0
# strand1 = "GAG"
# strand2 = ""                    Raise a ValueError


def hamming_distance(strand1, strand2):
    
    if len(strand1) != len(strand2):
        raise ValueError("Input strands must have the same length")
    differences = 0
    for i in range(len(strand1)):
        if strand1[i] != strand2[i]:
            differences += 1
    return differences

# if inputs arent always valid 

def hamming_distance(strand1, strand2):
    # Input Validation: Check if both strands have the same length.
    # This is essential because the Hamming distance is defined only for
    # sequences of equal length.
    if len(strand1) != len(strand2):
        raise ValueError("Input strands must have the same length")

    # Initialize a variable to count the differences
    differences = 0

    # Iterate through each character in the strands
    for i in range(len(strand1)):
        # Compare characters at the same position in both strands
        if strand1[i] != strand2[i]:
            # Increment the count if characters are different
            differences += 1

    # Return the total count of differences
    return differences

# Example usage
try:
    print(hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))  # Output: 7
    print(hamming_distance("GAG", "GAG"))  # Output: 0
    print(hamming_distance("GAG", ""))  # This will raise a ValueError
except ValueError as e:
    print(e)
    
    
# Time Complexity: O(n)
# The time complexity is O(n), where n is the length of the DNA strands
# (strand1 and strand2). This is because the function iterates through each
# character in the strands exactly once. The for-loop runs n times, and each
# operation inside the loop (checking characters and incrementing differences)
# has a constant time complexity.

# Space Complexity: O(1)
# The space complexity is O(1), meaning it is constant. This is because the
# function uses a fixed amount of space regardless of the input size. The only
# extra memory used is for the differences variable, a single integer, whose
# size does not change based on the length of the input strands.