alpha = ["a", "a", "b", "c", "c", "d", "c", "e", "d", "e"]
desc_alpha = []
new_alpha = []
for a in alpha:
    if a not in new_alpha:
        new_alpha.append(a)

for i in range(1, len(new_alpha)+1):
    desc_alpha.append(new_alpha[-i])

print(desc_alpha)
