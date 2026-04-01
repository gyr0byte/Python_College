word = list(input("Enter your word: ").lower())
rev_word = []
for i in range(1, len(word)+1):
    rev_word.append(word[-i])
if word == rev_word:
    print(f"The word is pallindrome")
else:
    print(f"The word is not pallindrome!")
