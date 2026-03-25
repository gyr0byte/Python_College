m = int(input("Enter the number of rows for the matrix: "))
n = int(input("Enter the number of colums for the matrix: "))
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)
        elif i < j:
            row.append(2)
        else:
            row.append(3)
    matrix.append(row)

for row in matrix:
    print(row)
