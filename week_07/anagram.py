word1 = list(input("Enter your first word: "))
word2 = list(input("Enter your second word: "))
word1.sort()
word2.sort()
if word1 == word2:
    print(f"The Given words are anagram!!")
else:
    print(f"The given words are not anagram")