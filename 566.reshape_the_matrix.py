unpack_before = [[1, 2, 3], [4, 5, 6]]

def reshape_matrix(mat, r, c):
    m, n = len(mat), len(mat[0])

    if m * n != r * c:
        return mat

    ans = [[0] * c for _ in range(r)]
    print('ans: ', ans)
    for i in range(m * n):
        ans[i // c][i % c] = mat[i // n][i % n]

    return ans

