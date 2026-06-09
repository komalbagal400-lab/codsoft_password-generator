import random
import string

# User Input
length = int(input("Enter password length: "))

# Characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# Generate Password
password = ""
for i in range(length):
    password += random.choice(characters)

# Display Password
print("Generated Password:", password)