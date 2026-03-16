nums = []
n = int(input("How many elements do you want to enter?"))
for i in range(n):
    num = int(input(f"Enter your {i+1} number: "))
    nums.append(num)

temp = 0
asce_list = nums.copy()
desc_list = nums.copy()
for i in range(n):
    for j in range(n):
        if asce_list[i] < asce_list[j]:
            temp = asce_list[j]
            asce_list[j] = asce_list[i]
            asce_list[i] = temp
        
for i in range(n):
    for j in range(n):
        if desc_list[i] > desc_list[j]:
            temp = desc_list[j]
            desc_list[j] = desc_list[i]
            desc_list[i] = temp
            
print(asce_list)
print(desc_list)