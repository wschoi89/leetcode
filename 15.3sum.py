from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for num in range(0, len(nums) - 2):
            if num > 0 and nums[num] == nums[num - 1]:
                continue
            value_i = nums[num]

            idx_left = num + 1
            idx_right = len(nums) - 1

            while idx_left < idx_right:
                value_j = nums[idx_left]
                value_k = nums[idx_right]

                sum = value_i + value_j + value_k

                if sum == 0:
                    result.append([value_i, value_j, value_k])
                    idx_left += 1

                    while nums[idx_left] == nums[idx_left - 1] and idx_left < idx_right:
                        idx_left += 1

                    while nums[idx_right] == nums[idx_right - 1] and idx_left < idx_right:
                        idx_right -= 1

                elif sum > 0:
                    idx_right -= 1

                else:
                    idx_left += 1

        return result