#Write a python program to add floating point numbers and complex numbers.
float_input = float(input("Enter a float:"))
complex_input = complex(input("Enter a complex number:"))
add_complex = complex_input + complex_input
add_float_complex = float_input + complex_input
print(add_complex, add_float_complex)
