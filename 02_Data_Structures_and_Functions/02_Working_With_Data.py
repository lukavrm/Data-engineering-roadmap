# ITERATING OVER LISTS

numbers = [10, 5, 8, 3, 12]

print("Numbers in the list:")
for number in numbers:
    print(number)

# SIMPLE LIST FILTERS AND SEARCHES

print("\nFiltering numbers greater than 7:")
greater_than_7 = []

for number in numbers:
    if number > 7:
        greater_than_7.append(number)

print("Filter result:", greater_than_7)

# Check whether a value is in the list

search_value = 8
if search_value in numbers:
    print(f"The value {search_value} is in the list.")
else:
    print(f"The value {search_value} is not in the list.")

# ITERATING OVER DICTIONARIES

student = {
    "name": "Anna",
    "age": 22,
    "major": "Mathematics"
}

print("\nIterating over the student dictionary keys:")
for key in student:
    print(f"{key} -> {student[key]}")

print("\nIterating over the student dictionary items:")
for key, value in student.items():
    print(f"{key}: {value}")

# SORTING AND TRANSFORMING DATA

print("\nOriginal list:", numbers)

ascending = sorted(numbers)  # Sorts the list in ascending order
descending = sorted(numbers, reverse=True)  # Sorts the list in descending order

print("List sorted in ascending order:", ascending)
print("List sorted in descending order:", descending)

# Transformation: create a new list containing the squares of the numbers

squares = []
for number in numbers:
    squares.append(number ** 2)

print("Squares of the numbers:", squares)