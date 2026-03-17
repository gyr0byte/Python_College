nums = [1,1,2,3,4,5,5,6,6,7,7]
revnums = []
newnums = []
for i in range(0, len(nums)):
    if nums[i] in newnums:
        continue
    else:
        newnums.append(nums[i])
for i in range(1, len(newnums)+1):
    revnums.append(newnums[-i])
print(newnums)
print(revnums)