import random
import string

def generate_password(length, use_special_chars):
    
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    use_special_chars = input("Do you want to include special characters? (yes/no): ").lower() == 'yes'
    password = generate_password(length, use_special_chars)
    print("Generated Password:", password)
