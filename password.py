import random
import string

def generate_password(length):
    # Characters to choose from: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters for the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
try:
    length = int(input("Enter the desired password length: "))
    if length <= 0:
        print("Password length must be a positive integer.")
    else:
        # Generate and display password
        generated_password = generate_password(length)
        print(f"Generated password: {generated_password}")
except ValueError:
    print("Please enter a valid integer for the password length.")
