# Lists (list)
# A list is a mutable, ordered collection that allows duplicate items.

fruits = ["apple", "banana", "orange", "grape", "pineapple"]
print("Fruit list:", fruits)

# Access by index (starts at 0)
print("First fruit:", fruits[0])  # apple
print("Last fruit:", fruits[-1])  # pineapple

# Common list methods:
fruits.append("mango")  # Adds "mango" to the end of the list
fruits.insert(1, "kiwi")  # Adds "kiwi" at index 1
fruits.remove("banana")  # Removes "banana" from the list

print("Updated fruits:", fruits)
print("Number of fruits:", len(fruits))  # List length

# TUPLES (tuple)
# A tuple is an immutable, ordered collection that allows duplicate items.
# Tuples are useful for data that should not change, such as geographic coordinates or RGB colors.

coordinates = (10, 20)
print("Coordinates:", coordinates)
print("x =", coordinates[0])
print("y =", coordinates[1])

# SETS (set)
# A set is a mutable, unordered collection that does not allow duplicate items.
# Sets are useful for representing mathematical sets, unique values, and similar data.

numbers = {1, 2, 3, 4, 5, 5}  # The duplicate 5 is ignored because sets do not allow duplicates
print("Set of numbers:", numbers)

numbers.add(6)  # Adds 6 to the set
numbers.add(2)  # Tries to add 2 again, but has no effect
print("Updated set of numbers:", numbers)
numbers.remove(3)  # Removes 3 from the set
print("Updated set of numbers:", numbers)

even_numbers = {2, 4, 6, 8}

print("Union:", numbers.union(even_numbers))  # Union of two sets
print("Intersection:", numbers.intersection(even_numbers))  # Intersection of two sets
print("Difference:", numbers.difference(even_numbers))  # Difference between two sets

# DICTIONARIES (dict)
# A dictionary is a mutable collection that stores key-value pairs.
# Dictionaries are useful for representing structured data, such as information about a person or a product.

student = {
    "name": "John",
    "age": 20,
    "major": "Engineering",
    "grades": [8.5, 7.0, 9.0]
}

print("Student information:", student)
print("Name:", student["name"])
print("Age:", student["age"])  # Accesses the value associated with the "age" key

# Add a new key-value pair
student["email"] = "john@email.com"
print("Updated student:", student)

# Useful methods

print("Keys:", student.keys())  # Returns all dictionary keys
print("Values:", student.values())  # Returns all dictionary values
print("Items:", student.items())  # Returns all key-value pairs