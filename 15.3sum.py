from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    result = []

    nums.sort()

    for i in range(len(nums) - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while nums[left] == nums[left - 1] and left < right:
                    left += 1

                while nums[right] == nums[right + 1] and left < right:
                    right -= 1

            elif nums[i] + nums[left] + nums[right] > 0:
                right -= 1

            else:
                left += 1

    return result


