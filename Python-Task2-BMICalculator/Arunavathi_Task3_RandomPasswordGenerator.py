import random
import string

print("===== Random Password Generator =====")

while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8 characters.")
            continue

        print("\nChoose character types:")
        print("1. Uppercase letters")
        print("2. Lowercase letters")
        print("3. Numbers")
        print("4. Symbols")

        choices = input("Enter choices (example: 1234): ")

        characters = ""

        if "1" in choices:
            characters += string.ascii_uppercase
        if "2" in choices:
            characters += string.ascii_lowercase
        if "3" in choices:
            characters += string.digits
        if "4" in choices:
            characters += string.punctuation

        if characters == "":
            print("Please select at least one character type.")
            continue

        password = "".join(random.choice(characters) for _ in range(length))

        print("\nGenerated Password:", password)

        again = input("\nGenerate another password? (yes/no): ")

        if again.lower() != "yes":
            print("Thank you!")
            break

    except ValueError:
        print("Invalid input! Please enter numbers only.")