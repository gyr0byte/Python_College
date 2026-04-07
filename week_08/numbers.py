lst = []
with open("week_08/lab8.txt", "r") as file:
    for data in file:
        if data.strip():
            lst.extend(int(x.strip())
                       for x in data.strip().split(",") if x.strip())
sum = 0
min = lst[0]
max = lst[0]
for nums in lst:
    sum += nums
    if nums < min:
        min = nums
    elif nums > max:
        max = nums

print(f"The sum of all numbers are {sum}")
print(f"The max is {max} and the min is {min}")
