# WHAT ARE FUNCTIONS?

# Functions are reusable blocks of code.
# They are used to:
# - Avoid repeating code
# - Organize a program
# - Give clear names to specific actions

# CREATING FUNCTIONS WITH def

def say_hello():
    print("Hello! Welcome to the Python course.")

def personalized_greeting(name):
    """Prints a greeting using the given name."""
    print(f"Hello, {name}! Nice to see you here.")

# Calling the functions

say_hello()
personalized_greeting("Lucas")

# PARAMETERS AND RETURN VALUES (return)

def add(a, b):
    """Returns the sum of two numbers."""
    result = a + b
    return result

example_sum = add(10, 5)
print("\nSum (10 + 5):", example_sum)

def calculate_average(numbers):
    """Returns the average of a list of numbers."""
    if len(numbers) == 0:  # If the list is empty, return 0
        return 0
    return sum(numbers) / len(numbers)

example_average = calculate_average([7, 8, 9])
print("\nAverage of [7, 8, 9]:", example_average)

# FUNCTIONS WITH DEFAULT VALUES

def introduce_person(name, age=18, city="Not provided"):
    """
    Example of a function with default values.
    If age or city is not provided, the default values are used.
    """
    print(f"Name: {name}, age: {age}, city: {city}")

print("\nIntroductions:")

introduce_person("John")
introduce_person("Mary", 25)
introduce_person("Charles", 30, "Rio de Janeiro")