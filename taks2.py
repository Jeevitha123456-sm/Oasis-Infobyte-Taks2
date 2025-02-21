import random
import string

def generate_password(length):
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Get the desired password length from the user
length = int(input("Enter the desired password length: "))

# Generate and display the password
password = generate_password(length)
print("Generated Password:", password)
