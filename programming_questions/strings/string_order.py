import sys
lines = sys.stdin.readlines()
words = [line.strip() for line in lines]
filtered_words = [word for word in words if word.isalpha()]

print(sorted(filtered_words))
