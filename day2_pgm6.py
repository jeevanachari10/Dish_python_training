#Write a python program to retrieve string which is repeated for more than once in the Paragraph. And store the resultant string to list.
#------------logic1--------------without using any library--------------
#import re
mystring = "This is an example for the checking repeating words. We check the repeated words in this sentence. We will store the repeated words in a list."

delimiters = ".,;:-!"    #defining delimiters we want to remove any punctuation
words = mystring.translate(str.maketrans('', '', delimiters))
words = words.lower()
#words = re.sub(r'[^\w\s]', '', mystring.lower()) #we can get the exct output importing regular expression library
#print(words)
mystring_list = words.split()    #converting sentence into list of words
#print(mystring_list)
seen_words = set()                #Using set as set won't allow duplicates
repeated_words = set()
for word in mystring_list:
    if word in seen_words:
        repeated_words.add(word)
    else:
        seen_words.add(word)

print(list(repeated_words))        #printing in the form of list


#-------------logic2--------------using libraries of regex and counter from collections-----------
from collections import Counter
import re

def find_repeated_strings(sentence):
    # Spliting the sentence into words using regex to handle punctuation
    words = re.findall(r'\b\w+\b', paragraph.lower())  # Using lowercase for case-insensitivity
    word_count = Counter(words)        # Count occurrences of each word using Counter
    repeated_strings = [word for word, count in word_count.items() if count > 1]    # Find words repeated more than once
    return repeated_strings

mystring = "This is an example for the checking repeating words. We check the repeated words in this sentence. We will store the repeated words in a list."
result_list = find_repeated_strings(mystring)
print(result_list)
