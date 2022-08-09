# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

'''
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
from typing import List

temp = [-2, 1, -3, 4]

nums = [-2, -3, 4, -1, -2, 1, 5, -3]


# 1. bruteforce
# def maxSubArray(nums: List[int]) -> int:
#     # 모든 subarray 구하기
#     maximum = []
#
#     for i in range(len(nums)):
#         comb = []
#         for j in range(i+1, len(nums) + 1):
#             comb.append(nums[i:j])
#         max_local = max([sum(x) for x in comb])
#
#         maximum.append(max_local)
#     return max(maximum)
#
# print(maxSubArray(nums))

# 2. kadene's algorithm
nums = [-3, 2, 5, -1]

local_max = nums[0]
global_max = nums[0]

for i in range(1, len(nums)):
    local_max = max(nums[i], local_max+nums[i])
    print('local_max: ', local_max)

    if local_max >= global_max:
        global_max = local_max

print('global_max: ', global_max)




# max_sub = -10000 - 1
# max_ending = 0
#
# for i in range(0, len(a)):
#     max_ending = max_ending + a[i]
#     if max_sub < max_ending:
#         max_sub = max_ending
#
#     if max_ending < 0:
#         max_ending = 0
#
# print(max_sub)


