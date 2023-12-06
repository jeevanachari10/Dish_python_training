#Write a python program to reverse a string.
string_input = input("Enter a string:")
#we can use below logic as well
#reverse_string = string_input[::-1] ; print(reverse_string)
string_list = list(string_input)
string_list.reverse()
string_input = "".join(string_list)
print(string_input)
