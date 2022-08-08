'''
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''

nums = [1, 2, 3, 4]

result = [0 for _ in range(len(nums))]
print(result)

for i in range(len(result)):
    temp = 1
    for j in range(len(result)):
        if i == j:
            continue

        temp *= nums[j]
    result[i] = temp

print(result)



