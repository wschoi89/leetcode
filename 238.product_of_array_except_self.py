'''
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''

nums = [1, 2, 3, 4]

tmp = 1
result = []
for num in nums:
    result.append(tmp)
    tmp *= num

tmp = 1
for idx in range(len(nums) - 1, -1, -1):
    result[idx] = result[idx] * tmp
    tmp *= nums[idx]

print(result)


