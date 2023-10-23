import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 51. N-Queens


def solveNQueens(n):
    def is_safe(board, row, col):
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 'Q':
                return False

        for i in range(row, -1, -1):
            if board[i][col] == 'Q':
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(["".join(row) for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(0)
    return solutions

# END


n = 5
queens_solutions = solveNQueens(n)
for solution in queens_solutions:
    for row in solution:
        print(row)
    print()
