"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the input we are trying to convert is not a valid integer
2. When will a ZeroDivisionError occur?
When the 2nd number is 0, and you try to divide
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, don't divide by 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")