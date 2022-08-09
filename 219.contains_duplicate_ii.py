# Given an integer array nums and an integer k,
# return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1
# Input: nums = [1, 2, 3, 1], k=3
# Output: true
from typing import List



def containsNearbyDuplicate(nums: List[int], k: int) -> bool:

        dic_ = dict()

        for i, v in enumerate(nums):
            if v in dic_.keys() and (i - dic_[v]) <= k:
                return True
            else:
                dic_[v] = i


print(containsNearbyDuplicate([1,0,1,1], 1))
