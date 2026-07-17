# Ask the user for their age
age = int(input("Enter your age: "))

# Store a Boolean value
is_adult = age >= 18

# Display the Boolean
print("Is Adult:", is_adult)

# Decide ticket price
if is_adult:
    print("Ticket Price: Ksh 500")
else:
    print("Ticket Price: Ksh 250")
