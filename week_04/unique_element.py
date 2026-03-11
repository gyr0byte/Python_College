nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 5, 6]
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