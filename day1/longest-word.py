sentence = "Python is an interpreted, high-level, general-purpose programming language."
words = sentence.split()

print(words)

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word: " + longest)