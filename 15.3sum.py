
# nums = [-1, 0, 1, 2, -1, 4]
# nums = [0, 1, 1]
nums = [0, 0, 0]


nums.sort()

print(nums)

result = []
for i in range(0, len(nums)-2):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1, len(nums)):
            if nums[i]+nums[j]+nums[k] == 0 and not [nums[i], nums[j], nums[k]] in result:
                result.append([nums[i], nums[j], nums[k]])

print('result: ', result)
