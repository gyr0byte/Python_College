n = int(input("How many numbers will you like to input? "))
listnum = []
for i in range(n):
    num = int(input(f"Enter the {i+1} Number "))
    listnum.append(num)
    
min = listnum[0]
max = listnum[0]
for num in listnum:
    if max < num:
        max = num
    elif min > num:
        min = num
            
print(f"The minimum value your list is {min}")
print(f"The maximum value your list is {max}")
print(listnum)