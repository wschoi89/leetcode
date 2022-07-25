board = \
[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

# dict 로 진행
def isValidSudoku(board) -> bool:
    n_rows = 9
    n_cols = 9

    # row 검증
    for r in range(n_rows):
        dict_ = dict()
        for c in range(n_cols):
            if board[r][c].isnumeric():
                dict_[board[r][c]] = dict_.get(board[r][c], 0) + 1

                if dict_[board[r][c]] == 2:
                    return False

        # 9칸 검증
        if r % 3 == 2:
            for iter in range(3):
                dict_9 = dict()

                for sub_r in range(r-2, r+1):
                    for sub_c in range(3*iter, 3*iter+3):
                        if board[sub_r][sub_c].isnumeric():
                            dict_9[board[sub_r][sub_c]] = dict_9.get(board[sub_r][sub_c], 0) + 1

                            if dict_9[board[sub_r][sub_c]] == 2:
                                return False

    # column 검증
    for c in range(n_cols):
        dict_ = dict()
        for r in range(n_rows):

            if board[r][c].isnumeric():
                dict_[board[r][c]] = dict_.get(board[r][c], 0) + 1

                if dict_[board[r][c]] == 2:
                    return False

    return True



print(isValidSudoku(board))



