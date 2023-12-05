#Write a python program to display portion of string for n times.
input_string = input("Enter a string:")
num_times = int(input("Enter the number of times the portion string should disply:"))

portion = len(input_string) // num_times
for i in range(n):
  print(input_string[:portion])
