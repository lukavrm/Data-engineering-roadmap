# Variables are "boxes" that store values.
# In Python, you do not need to declare the variable type explicitly; it is automatically determined based on the assigned value.

name = "João"  # String - text type
age = 30       # Integer - whole number type
height = 1.75  # Float - decimal number type
does_have_driver_license = True  # Boolean - true/false type

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Does the person have a driver's license?", does_have_driver_license)


# Data types in Python
# String (str): Represents text. Example: "Hello, world!"
# Integer (int): Represents whole numbers. Example: 42
# Float (float): Represents decimal numbers. Example: 3.14
# Boolean (bool): Represents logical values. Example: True or False

# Mathematical operations
a = 10
b = 3

print("Sum:", a + b)            # Addition
print("Subtraction:", a - b)     # Subtraction
print("Multiplication:", a * b)  # Multiplication
print("Division:", a / b)        # Division
print("Integer division:", a // b)  # Integer division
print("Remainder:", a % b)       # Modulo
print("Exponentiation:", a ** b) # Exponentiation

# String concatenation
first_name = "Ana"
last_name = "Silva"
full_name = first_name + " " + last_name
print("Full name:", full_name)

# f-strings (string formatting)
age = 25
message = f"Hello, {full_name}! I am {age} years old."
print(message)