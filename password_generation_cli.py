import random
import string

def generate_password(length):
    """
    Generates a strong random password of given length.
    Ensures at least one lowercase, uppercase, digit, and symbol.
    """
    if length < 4:
        return "Password length should be at least 4"

    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation


    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    
    all_chars = lower + upper + digits + symbols
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    
    random.shuffle(password)

    return ''.join(password)

def main():
    print("=== Python Password Generator (CLI) ===")
    try:
        length = int(input("Enter the length of your password: "))
        password = generate_password(length)
        print("\nGenerated Password:", password)
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()