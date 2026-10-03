"""
Objectives:
- Understand variable scope.
- Create small, reusable functions.
- Discuss naming and code organization.
"""

# VARIABLE SCOPE

global_message = "I am a global variable."

def scope_example():
    local_message = "I am a local variable."
    print(global_message)  # Accesses the global variable
    print(local_message)  # Accesses the local variable

scope_example()

# print(local_message)  # This would raise an error because it does not exist outside the function

# SMALL, REUSABLE FUNCTIONS

# Rule of thumb:
# - A function should do one well-defined thing.
# - If it does too many things, it probably needs to be split up.

def calculate_discount(price, percentage):
    return price - (price * percentage / 100)

def format_currency(value):
    return f"USD {value:.2f}"

original_price = 100
discounted_price = calculate_discount(original_price, 10)

print("\nOriginal price:", format_currency(original_price))
print("\nDiscounted price:", format_currency(discounted_price))

# NAMING AND CODE ORGANIZATION

"""Best practices:
- Function names: verb + object
    e.g. calculate_total, find_customer, send_email
- Variable names: clear and descriptive
    e.g. item_quantity, unit_price, grade_average
- Avoid:
    overly generic names: x, y, a1, data
    overly large functions
- Using English names is a good practice.
"""

def sum_list(numbers):
    """Returns the sum of a list of numbers."""
    return sum(numbers)

def calculate_list_average(numbers):
    """Returns the average of a list of numbers."""
    if not numbers:
        return 0
    return sum_list(numbers) / len(numbers)

example_list = [5, 7, 9]

print("\nExample list:", example_list)
print("Sum:", sum_list(example_list))
print("Average:", calculate_list_average(example_list))




