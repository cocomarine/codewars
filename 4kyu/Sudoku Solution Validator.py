def valid_solution(board):

    correct = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Row check: going through the rows in sudoku board and check
    # if numbers 1-9 are there by sorting and comparing it with numbers list
    for row in board:
        if sorted(row) != correct:
            return False

    # Column check: creating tuples of column using zip function and then check
    for column in zip(*board):
        if sorted(column) != correct:
            return False

    # 3 x 3 block generation and check:
    # one for-loop is used (i) to iterate board 3 lines at a time
    # i.e. when i = 0, board[0:3], when i = 1, board[3:6] etc.
    # another for-loop used (j) to iterate three columns at a time
    # i.e. when j = 0, line[0:3], when j = 1, line[3:6] etc.
    for i in range(3):
        for j in range(3):
            block = []
            for line in board[i*3:(i+1)*3]:
                block += line[j*3:(j+1)*3]

            # block check
            if sorted(block) != correct:
                return False

    return True