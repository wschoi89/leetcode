from typing import List, Optional

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# output = [1, 1, 1, 0]


def dailyTemperatures(temperatures: List[int]) -> List[int]:

    result = [0] * len(temperatures)

    stack = []

    for i, t in enumerate(temperatures):

        while stack and stack[-1][0] < t:
            result[stack[-1][1]] = i - stack[-1][1]
            stack.pop()

        else:
            stack.append([t, i])

    return result




result = dailyTemperatures(temperatures)
print('result: ', result)





