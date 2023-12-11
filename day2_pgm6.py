#Write a python program to retrieve string which is repeated for more than once in the Paragraph. And store the resultant string to list.
from collections import Counter
import re

def find_repeated_strings(paragraph):
    # Split the paragraph into words using regex to handle punctuation
    words = re.findall(r'\b\w+\b', paragraph.lower())  # Using lowercase for case-insensitivity
    
    # Count occurrences of each word using Counter
    word_count = Counter(words)
    
    # Find words repeated more than once
    repeated_strings = [word for word, count in word_count.items() if count > 1]
    
    return repeated_strings

# Example paragraph
paragraph = "This is a paragraph. This paragraph contains repeated words. Words like this are repeated."

# Retrieve repeated strings
result_list = find_repeated_strings(paragraph)

print("Strings repeated more than once in the paragraph:")
print(result_list)
