import random

def generate_pass(length):
    easy = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    middle = "abcdefghijklmnopqrstuvwxyz12345678910ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hard = "abcdefghijklmnopqrstuvwxyz12345678910ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*-+"

    while True:
        try:
            lvl = int(input("1 - password without symbols and numbers\n2 - password just without symbols\n3 - full password(with numbers and special characters)\nSelect the password difficulty level: "))
            if lvl not in [1, 2, 3]:
                raise ValueError("Invalid input. Please enter a number between 1 and 3.")

            if not isinstance(length, int) or length <= 0:
                raise ValueError("Invalid input. Please enter a positive integer for password length.")

            match lvl:
                case 1:
                    password = "".join(random.sample(easy, length))
                case 2:
                    password = "".join(random.sample(middle, length))
                case 3:
                    password = "".join(random.sample(hard, length))

            return password
        except ValueError as e:
            print(f"Error: {e}")

try:
    while True:
        try:
            password_length = int(input("Enter the length of the password: "))
            if password_length > 0:
                break
            else:
                print("Invalid input. Please enter a positive integer for password length.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for password length.")

    print('Your generated password:', generate_pass(password_length))
except ValueError:
    print("Invalid input. Please enter a positive integer for password length.")

