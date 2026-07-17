# Ask the user to enter their full name
full_name = input("Enter your full name: ")

# Split the name into parts
name_parts = full_name.split()

# Check if the user entered two or more names
if len(name_parts) >= 2:
    print(f"Hello, {name_parts[0]}! Welcome.")
else:
    print("Please enter your full name (first and last name).")
