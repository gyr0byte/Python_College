a = [2, 3, 6, 8, 9, 12, 15, 18, 24, 22, 33, 112]
newlist = []
for n in a:
    if n % 3 == 0 and n % 2 == 0:
        newlist.append(n)
    else:
        continue
    
print(newlist)