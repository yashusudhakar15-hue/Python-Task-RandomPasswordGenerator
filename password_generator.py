
import random
import string

print("================================")
print("    RANDOM PASSWORD GENERATOR")
print("================================")

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Error: Password length must be positive.")

    elif length < 4:
        print("Error: Password length must be at least 4.")

    else:
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for i in range(length))

        print("\nGenerated Password:", password)

except ValueError:
    print("Error: Please enter a valid number.")
