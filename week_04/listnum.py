n = int(input("How many numbers will you like to input?"))
listnum = []
for i in range(n):
    num = int(input(f"Enter the {i+1} Number"))
    listnum.append(num)
sum = 0
for nums in listnum:
    sum += nums

print(f"The sum of your list is {sum}")
