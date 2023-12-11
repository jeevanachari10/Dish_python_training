#Write a python program to retrieve string which is repeated for more than once in the Paragraph. And store the resultant string to list.
#--------------------------------Logic1-----------------------------------------------
#import re
mystring = "This is an example for the checking repeating words. We check the repeated words in this sentence. We will store the repeated words in a list"

delimiters = ".,;:-!"
words = mystring.translate(str.maketrans('', '', delimiters))
words = words.lower()
#words = re.sub(r'[^\w\s]', '', mystring.lower())
#words = re.sub(r'\b\w+\b', '', mystring.lower())
print(words)
mystring_list = words.split()
print(mystring_list)
seen_words = set()
repeated_words = set()
for word in mystring_list:
    if word in seen_words:
        repeated_words.add(word)
    else:
        seen_words.add(word)

print(list(repeated_words))
#------------------------------------------------logic2----------------------------------------------
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
