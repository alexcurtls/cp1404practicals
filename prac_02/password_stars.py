"""Password checking"""

minimum_length = 1
password = input("Enter password: ")
while len(password) < minimum_length:
    print("Invalid")
    password = input("Enter password: ")
print("*" * len(password))

