a = [
    [24, 3, 6],
    [8, 12, 18],
    [2, 66, 7]
]
max = a[0][0]
min = a[0][0]
for i in a:
    for j in i:
        if j % 2 == 0 and j % 3 == 0:
            print(j)
        if j > max:
            max = j
        elif j < min:
            min = j

print(f"maximum value is {max}")
print(f"minimum value is {min}")
