"""Password checking"""

def main():
    minimum_length = 8
    password = get_password(minimum_length)
    print_password(password)


def print_password(password):
    print("*" * len(password))


def get_password(minimum_length):
    password = input("Enter password: ")
    while len(password) < minimum_length:
        print("Invalid")
        password = input("Enter password: ")
    return password


main()

