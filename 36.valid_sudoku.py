# 3rules
from typing import List
from collections import defaultdict
board = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def isValidSudoku(board: List[List[str]])->bool:
    dict_rows = defaultdict(set)
    dict_cols = defaultdict(set)
    dict_box = defaultdict(set)

    rows, cols = len(board), len(board[0])

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == '.':
                continue

            if (board[r][c] in dict_rows[r]) or (board[r][c] in dict_cols[c]) or (board[r][c] in dict_box[(r // 3,c // 3)]):
                return False
            else:
                dict_rows[r].add(board[r][c])
                dict_cols[c].add(board[r][c])
                dict_box[(r//3,c//3)].add(board[r][c])

    print(dict_box)
    return True


print(isValidSudoku(board))
