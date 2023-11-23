import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1572. Matrix Diagonal Sum


def diagonalSum(mat):
    total = 0
    n = len(mat)

    for i in range(n):
        total += mat[i][i] + mat[i][n - 1 - i]

    if n % 2 == 1:
        total -= mat[n // 2][n // 2]

    return total


# END
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

result = diagonalSum(mat)
display(result)
