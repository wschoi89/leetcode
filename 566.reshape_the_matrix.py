unpack_before = [[1, 2, 3], [4, 5, 6]]
#
# unpack_after = [j for sub in unpack_before for j in sub]
#
# print(unpack_after)
#
#
# list_ = []
# for sub in unpack_before:
#     for j in sub:
#         list_.append(j)
#
# # 이중 for loop -> list comprehension 변환 시
# # 이중 loop은 순서대로 풀어 작성
#
#
# a = [j for sub in unpack_before for j in sub]


def reshape_matrix(mat, rows, cols):
    # print(len(mat), len(mat[0]))

    res = []
    index = 0
    m, n = len(mat), len(mat[0])

    flatten = [j for sub in mat for j in sub]

    if m*n != rows*cols:
        return mat

    for r in range(rows):
        temp = []
        for c in range(cols):
            temp.append(flatten[index])
            index += 1
        res.append(temp)

    return res


print(reshape_matrix(unpack_before, 3, 2))

