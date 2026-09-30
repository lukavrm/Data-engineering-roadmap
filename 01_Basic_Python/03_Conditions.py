name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello, {name}! You are {age} years old.")

# Comparison operators:
# == equal to
# != different from
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

# Logical operators:
# and
# or
# not

is_of_legal_age = age >= 18

print("Are you of legal age?", is_of_legal_age)

# Conditional structures:
if age < 12:
    category = "Child"
elif age < 18:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior"

print(f"Age category: {category}")

# Examples of logical operators:

does_have_driver_license = input("Do you have a driver's license? (yes/no) ").lower() == "yes"  # lower() converts the response to lowercase, and the comparison checks if the answer is "yes"
does_have_car = input("Do you have a car? (yes/no) ").lower() == "yes"

if does_have_driver_license and does_have_car:
    print("You can drive your car.")
elif does_have_driver_license and not does_have_car:
    print("You have a driver's license, but no car.")
elif not does_have_driver_license and does_have_car:
    print("You have a car, but no driver's license.")
else:
    print("You do not have a driver's license or a car.")