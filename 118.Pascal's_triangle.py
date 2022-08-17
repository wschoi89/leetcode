from typing import List


def generate(num_rows: int)->List[List[int]]:

    result = [[1]*i for i in range(1, num_rows+1)]
    print(result)

    if num_rows <=2:
        return result

    for i in range(2, num_rows):
        for j in range(1, i):
            result[i][j] = result[i-1][j-1] + result[i-1][j]
    print(result)

generate(5)
