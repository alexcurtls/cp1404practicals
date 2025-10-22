"""
Word Occurrences
Estimate: 25 minutes
Actual: 20 minutes
"""



text = input("Text: ")

word_to_letters = list(text)

print(word_to_letters)

counts = {}
for w in word_to_letters:
    counts[w] = counts.get(w, 0) + 1


for word, count in counts.items():
    print(word, ":", count)

