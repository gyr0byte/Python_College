alpha1 = ["a", "b", "c", "d", "e"]
alpha2 = ["f", "g", "h", "i", "j"]
added = []
for i in range(len(alpha2)):
    added.append(alpha1[i] + alpha2[i])

print(added)
