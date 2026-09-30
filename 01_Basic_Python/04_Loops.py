# while loop

# while executes WHILE the condition is true

counter = 1

print("Counting from 1 to 7 with while:")
while counter <= 7:
    print("counter =", counter)
    counter += 1  # Increments the counter by 1

# Example: ask for the password until it is correct

correct_password = "python123"
try_password = input("Enter the password: ")

while try_password != correct_password:  # While the attempt is different from the correct password, the loop continues
    print("Incorrect password. Try again.")
    try_password = input("Enter the password: ")

print("Correct password! Access granted.")

# for loop

# for is often used to iterate over lists and ranges

print("\nIterating through a list with for:")
fruits = ["apple", "banana", "orange"]

for fruit in fruits:  # For each element in the fruits list, the variable fruit receives the current element value
    print("Fruit:", fruit)

print("\nUsing range to generate numbers:")
for number in range(1, 6):  # Generates numbers from 1 to 5
    print("Number:", number)

# Break and continue

print("\nExample of break:")
for number in range(1, 10):
    if number == 5:
        print("I reached number 5, I'm leaving the loop")
        break  # Exits the loop when the number is 5
    print("Number:", number)

print("\nExample of continue:")
for number in range(1, 10):
    if number == 5:
        # print("Skipping number 5")
        continue  # Skips to the next iteration when the number is 5
    print("Number:", number)
