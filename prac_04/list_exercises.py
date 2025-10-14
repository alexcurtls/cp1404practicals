
def main():
    numbers = []
    for i in range(1, 6):
        while True:
            try:
                number_value = float(input(f"Number: {i}" ))
                numbers.append(number_value)
                break
            except ValueError:
                print(f"Enter a valid number: ")

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)} ")
    print(f"The average of the numbers is {sum(numbers)}")