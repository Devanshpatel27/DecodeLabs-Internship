import random
import string

def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )
    return ''.join(random.choice(characters) for _ in range(length))

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Please enter a positive number.")

    else:
        password = generate_password(length)

        print("\n===== RANDOM PASSWORD GENERATOR =====")
        print("Generated Password:", password)

except ValueError:
    print("Invalid input! Please enter a valid number.")