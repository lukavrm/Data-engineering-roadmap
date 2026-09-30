# Ask for the age of several people and count:
# - How many people are under 18
# - How many people are 18 or older
# - The program must stop when the entered age is negative

print("=== Mini challenge: age counter ===")

people_under_18 = 0
people_18_or_more = 0

while True:  # infinite loop
    age_text = input("Enter an age (or a negative number to exit): ")  # asks the user for the age

    # Handling invalid input (non-numeric)
    if age_text.strip() == "":  # strip() removes whitespace at the beginning and end of the string, so if the input is empty, it enters this if
        print("You did not enter anything. Please try again.")
        continue  # skip to the next number / go back to the beginning and ask for the age again

    age = int(age_text)  # converting the input to an integer

    if age < 0:  # if it is negative, exit the loop
        print("Ending the count...")
        break
    if age < 18:  # if it is less than 18, add 1 to the under-18 counter
        people_under_18 += 1
    else:  # if it is greater than or equal to 18, add 1 to the 18-or-more counter
        people_18_or_more += 1

print("\n--- Result ---")
print("People under 18 years old:", people_under_18)
print("People 18 years old or older:", people_18_or_more)