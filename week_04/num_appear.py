nums = [1,2,6,4,5,7,6,7,8,1,4,5]
for i in nums:
    count = 0
    for j in nums:
        if i == j:
            count +=1
    if count >= 1:
        print(i, count)