# arr = [1, 3, 5]
# leetcode 1524



2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
def solution(arr):

    count_odd = 0
    count_even = 0
    result = 0
    m = 1000000007

    for value in arr:
        if value % 2 ==0:
            count_odd, count_even = count_odd, count_even+1
        else:
            count_even, count_odd = count_odd, count_even+1

        result = result+count_odd

    return result % m


# 정수 n이 주어졌을 때 합이 n이 되는 제곱의 최소개수

# https: // lakelouise.tistory.com / 61

2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
import math

def solution(n):

    if math.isqrt(n)**2 == n:
        return 1

    dp = [i for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, i):
            if (j**2) > i:
                break

            if dp[i] > dp[i-j**2]+1:
                dp[i] = dp[i-j**2] + 1

    return dp[n]

# question 3

2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
def solution(param0):
    keyboard = \
    {'A':[0, 0], 'B': [0, 1], 'C': [0, 2], 'D':[0, 3], 'E':[0,4], 'F':[0,5],
     'G':[1, 0], 'H': [1, 1], 'I': [1, 2], 'J':[1, 3], 'K':[1,4], 'L':[1,5],
     'M':[2, 0], 'N': [2, 1], 'O': [2, 2], 'P':[2, 3], 'Q':[2,4], 'R':[2,5],
     'S':[3, 0], 'T': [3, 1], 'U': [3, 2], 'V':[3, 3], 'W':[3,4], 'X':[3,5],
     'Y':[4, 0], 'Z': [4, 1],}

    # def eval_cost(cur, finger_1, finger_2):
    #     cost_1 = abs(cur[0] - finger_1[0]) + abs(cur[1] - finger_1[1])
    #     cost_2 = abs(cur[0] - finger_2[0]) + abs(cur[1] - finger_2[1])

    #     if cost_1 < cost2:
    #         return cost_1
    #     else:
    #         return cost_2



    cost = 0
    if len(param0) ==2:
        return cost

    finger_1 = None
    finger_2 = None

    for ch in param0:
        cur = keyboard[ch]

        if cur[1]<3:
            if finger_1 is None:
                finger_1 = cur
            else:
                cost = cost + abs(cur[0] - finger_1[0]) + abs(cur[1] - finger_1[1])
                finger_1 = cur

        else:
            if finger_2 is None:
                finger_2 = cur
            else:
                cost = cost + abs(cur[0] - finger_2[0]) + abs(cur[1] - finger_2[1])
                finger_2 = cur
    return cost



















print(solution_2(12))



