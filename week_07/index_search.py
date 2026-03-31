def locate_index(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target:
                return i, j
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = locate_index(arr, target)
print(result)
