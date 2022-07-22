def generate(numRows: int):
    result = [[1] * i for i in range(1, numRows+1)]

    for i in range(2, numRows):
        for j in range(1, i):
            result[i][j] = result[i-1][j] + result[i-1][j-1]

    return result

print(generate(4))