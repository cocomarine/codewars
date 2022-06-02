# Sudoku Background
# Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
# Sudoku Solution Validator
# Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.
# The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

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
