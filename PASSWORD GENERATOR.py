import random
import string

def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Password length must be at least 1. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    password = password_generator(length)
    
    print(f"Password Generator : {password}")

if __name__ == "__main__":
    main()
