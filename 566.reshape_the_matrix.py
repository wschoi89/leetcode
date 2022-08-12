unpack_before = [[1, 2, 3], [4, 5, 6]]

def reshape_matrix(mat, r, c):
    m, n = len(mat), len(mat[0])

    if m*n != r*c:
        return mat

    reshaped = [[0]*c for _ in range(r)]
    print(reshaped)

    for i in range(m*n):
        reshaped[i//c][i%c] = mat[i//n][i%n]
    print(reshaped)


reshape_matrix(unpack_before, 3, 2)

