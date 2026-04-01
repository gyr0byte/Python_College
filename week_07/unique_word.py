word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
unique_word1 = []
unique_word2 = []
for word in word1:
    if word not in word2:
        unique_word1.append(word)
for word in word2:
    if word not in word1:
        unique_word2.append(word)
print(f"The unique letters in {word1} are {unique_word1}")
print(f"The unique letters in {word2} are {unique_word2}")