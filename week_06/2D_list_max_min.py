matrix1 = [[1, 2, 3],
           [8, 9, 4],
           [7, 6, 5]]

matrix2 = [[2, 7, 6],
           [9, 5, 1],
           [4, 3, 8]]
sum_dia = 0
sum_up = 0
sum_down = 0
for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        if i == j:
            sum_dia += matrix1[i][j] + matrix2[i][j]
        elif i < j:
            sum_up += matrix1[i][j] + matrix2[i][j]
        else:
            sum_down += matrix1[i][j] + matrix2[i][j]
max_matrix1 = matrix1[0][0]
min_matrix1 = matrix1[0][0]
max_matrix2 = matrix2[0][0]
min_matrix2 = matrix2[0][0]

for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        if matrix1[i][j] > max_matrix1 and matrix2[i][j] > max_matrix2:
            max_matrix1 = matrix1[i][j]
            max_matrix2 = matrix2[i][j]

        elif matrix1[i][j] < min_matrix1 and matrix2[i][j] < min_matrix2:
            min_matrix1 = matrix1[i][j]
            min_matrix2 = matrix2[i][j]

print(sum_dia)
print(sum_up)
print(sum_down)
print(f"maximum value of matrix2 is {max_matrix1}")
print(f"minimum value of matrix2 is {min_matrix1}")
print(f"maximum value of matrix1 is {max_matrix2}")
print(f"minimum value of matrix1 is {min_matrix2}")
