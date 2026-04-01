word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
common_word = []
for word in word1:
    if word in word2:
        common_word.append(word)

print(common_word)
