# Given an integer array nums and an integer k,
# return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1
# Input: nums = [1, 2, 3, 1], k=3
# Output: true
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = dict()

        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            else:
                dic[v] = i
        return False
    