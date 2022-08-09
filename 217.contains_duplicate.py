from typing import List

'''
nums = [1, 2, 3, 1]
Output = true

'''


def contain_duplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))


data = [1, 2, 3, 1]
print(contain_duplicate(data))

