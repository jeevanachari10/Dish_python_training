#Write a python program to display portion of string in reversing order.
string_input = input("Enter a string:")
portion_start = int(input("Enter the start and end position:"))
portion_end = int(input("Enter the end position:"))
portion_string = string_input[portion_start:portion_end]
reverse_string = portion_string[::-1]
print(reverse_string)
