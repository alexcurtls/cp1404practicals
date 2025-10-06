"""
CP1404/CP5632 - Practical 3
Files
"""


# 1.

FILENAME = "name_output.txt"

out_file = open(FILENAME, 'w')
name = input("Name: ")
print(f"{name:}", file=out_file)

out_file.close()

# 2.

infile = open(FILENAME, "r")
number = (infile.read())
print(f"Hi {name}!")
infile.close()



# 3.

FILENAME = "numbers.txt"

with open(FILENAME, "r") as infile:
    number_one = int(infile.readline())
    number_two = int(infile.readline())
    result = number_one + number_two
    print(result)

# 4.

total = 0
with open(FILENAME, "r") as infile:
    for line in infile:
        total += int(line.strip())
print(total)