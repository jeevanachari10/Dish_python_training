#Find palindrome of a string.
def is_palindrome(s):
    s = ''.join(e.lower() for e in s if e.isalnum())  #to get more accureate results few filters applied
    return s == s[::-1]

string_input = input("Enter a string:")
#logic 1
if string_input == string_input[::-1]:
  print(f"{string_input} is a palindrome")
else:
  print(f"{string_input} is not a palindrome")

#logic using funtions 
if is_palindrome(string_input):
    print(f"{string_input} is a palindrome")
else:
    print(f"{string_input} is not a palindrome")
