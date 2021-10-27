# For reference, this is based on Leetcode Problem No. 58 Length of Last Word
# https://leetcode.com/problems/length-of-last-word/ 
 
# Challenge:
 
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
# return the length of last word (last word means the last appearing word if we loop from 
# left to right) in the string.
 
# Format: "word_1 space word_2 space word_3 space ... space word_n"
 
# Note: A word is defined as a maximal substring consisting of non-space characters only.
 
 
# Examples: 
    # Example 1:
    # Input: "Hello World"
    # Output: 5
 
    # Example 2:
    # Input: "Hello"
    # Output: 5
 
    # Example 3:
    # Input: "   hello "
    # Output: 5
 
 
# Code:

# Take user input for input string and store it
user_input = input("Please enter a string and separate words with singular spaces: ")
 
# master function for easy modification and scalability
def master_length_of_lastWord(input):
    # Parse input and store it in an array/list
    parsed_input = input.split()
 
    # Initialize variable to store the length of the last word for clarity
    length_of_last_word = 0
 
    # Finding length of last word
        # Case 1: Length of the string is equal to 1 word
    if(len(parsed_input) == 0):
        # Set the length of the last word to 0
        length_of_last_word = 0
 
        # return length of the last word
        return length_of_last_word
 
        # Case 2: All other situations
            # Note: This also by default accounts for if there is a space after the 1 word in the string, but no actual word
    else:
        # Set the length of the last word to the length of the value in the last index of the array
            # Note: Since an array index starts at 0 and not 1, then the index at the length of the array is out of range
            # will give an out of range error.
            # So, we do - 1 to get the correct last index in the array.
        # Long-cut: length_of_last_word = len(parsed_input[len(parsed_input) - 1])
        # Short-cut: directly gets last index in the array
        length_of_last_word = len(parsed_input[-1])
 
        # return length of the last word
        return length_of_last_word
 
# Driver code:
print(master_length_of_lastWord(user_input))