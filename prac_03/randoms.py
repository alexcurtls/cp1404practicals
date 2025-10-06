"""
CP1404/CP5632 - Practical 3
Random Numbers
"""

import random

# "What did you see on line 1?"
# I ran it 5 times and saw 18, 12, 9, 7, 7
# The shortest I could've seen was 5 and the largest was 20

# "What did you see on line 2?"
# I ran it 5 times and saw 9, 3, 5, 5, 7
# The smallest I could've seen was 3 and the largest was 9
# It could not have produced a 4, as it seems like it picks from the sequence (3, 5, 7, 9)

# "What did you see on line 3?"
# I ran it 3 times and saw 5.2559..., 3.1686..., 4.2369...
# The smallest I could've seen was 2.5 and the larges was 5.4999? (the range doesn't usually include the end)

random_number = random.randint(1, 101)
print(random_number)