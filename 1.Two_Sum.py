# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

# Example

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# exactly one solution이 힌트. 즉 list에 같은 값이 없다는 의미 -> value가 key가 될 수 있음

def two_sum(nums, target):
    seen = {}

    for i, v in enumerate(nums):
        remain = target - v

        if remain in seen:
            return [seen[remain], i]
        else:
            seen[v] = i
