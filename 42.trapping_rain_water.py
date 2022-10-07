from typing import List


def trap(height: List[int])->int:
    if not height:
        return 0

    result = 0
    left_max, right_max = [0] * len(height), [0] * len(height)

    # left_max, right_max = height[0], max(height[1:])
    for i in range(1, len(height)):
        left_max[i] = max(left_max[i-1], height[i-1])

    for i in range(len(height)-2, -1, -1):
        right_max[i] = max((right_max[i+1], height[i+1]))

    for i in range(len(height)):
        water_level = min(left_max[i], right_max[i])

        if water_level >=height[i]:
            result += water_level - height[i]

    return result


height = [0,1,0,2,1,0,1,3,2,1,2,1] # answer = 6
# height = [4,2,0,3,2,5]

vol = trap(height)
print(vol)

