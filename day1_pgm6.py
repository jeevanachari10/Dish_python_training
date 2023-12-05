#Write a python program to reverse a string.
string_input = input("Enter a string:")
#reverse_string = string_input[::-1]
string_list = list(string_input)
string_list.reverse()
string_input = "".join(string_list)
print(string_input)
