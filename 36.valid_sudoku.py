# board = \
# [["5","3",".",".","7",".",".",".","."],
#  ["6",".",".","1","9","5",".",".","."],
#  [".","9","8",".",".",".",".","6","."],
#  ["8",".",".",".","6",".",".",".","3"],
#  ["4",".",".","8",".","3",".",".","1"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".","6",".",".",".",".","2","8","."],
#  [".",".",".","4","1","9",".",".","5"],
#  [".",".",".",".","8",".",".","7","9"]]

# board = \
#     [[".",".",".",".",".",".",".",".","."],
#      [".",".",".",".",".",".",".",".","."],
#      [".",".",".",".",".",".",".",".","."],
#      [".",".",".",".",".",".",".",".","."],
#      [".",".",".",".",".",".",".",".","."],
#      [".",".",".",".",".",".",".",".","."],
#      [".",".",".",".",".",".",".",".","."],
#      [".",".",".",".",".",".",".",".","."],
#      [".",".",".",".",".",".",".",".","."]]


board = \
[[".",".",".",".",".",".","5",".","."],
 [".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".","."],
 ["9","3",".",".","2",".","4",".","."],
 [".",".","7",".",".",".","3",".","."],
 [".",".",".",".",".",".",".",".","."],
 [".",".",".","3","4",".",".",".","."],
 [".",".",".",".",".","3",".",".","."],
 [".",".",".",".",".","5","2",".","."]]
from collections import Counter

# print(board)
# dict 로 진행
def isValidSudoku(board) -> bool:
    for row in board:
        counter = Counter(row)
        # print(counter)

        most_common = counter.most_common(2)
        print(len(most_common))

        if len(most_common) == 1 and most_common[0][0] == '.':
            continue
        if most_common[1][1] != 1:
            return False

        # rule2 (column check)

    columns = [[row[x] for row in board] for x in range(9)]

    for column in columns:
        counter = Counter(column)
        most_common = counter.most_common(2)
        if len(most_common) == 1 and most_common[0][0] == '.':
            continue
        if most_common[1][1] != 1:
            return False

    for c in range(0, 9, 3):
        for r in range(0, 9, 3):
            box = [board[i][j] for i in range(0 + c, 3 + c) for j in range(0 + r, 3 + r)]
            counter = Counter(box)
            most_common = counter.most_common(2)
            if len(most_common) == 1 and most_common[0][0] == '.':
                continue
            if most_common[1][1] != 1:
                return False

    return True


print(isValidSudoku(board))



