def counts():
    word = input("Enter the word: ")
    count_vowel = 0
    count_consonent = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in word:
        if (i in vowels):
            count_vowel += 1
        else:
            count_consonent += 1
    return "vowels", count_vowel, "Consonent", count_consonent

a = counts()
print(a)
