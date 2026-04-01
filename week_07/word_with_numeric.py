words = list(input("Enter the word with numeric value: "))
count = 0
consonent = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(len(words)):
    if words[i].isdigit():
        count += 1
    elif words[i] in vowels:
        continue
    else:
        consonent += 1
print(count)
print(consonent)
