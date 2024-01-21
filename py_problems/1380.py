import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1380. Lucky Numbers in a Matrix


def luckyNumbers(matrix):
    minRow = [min(x) for x in matrix]
    maxCol = [max(i) for i in zip(*matrix)]

    return set(minRow) & set(maxCol)


# END
matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]

result = luckyNumbers(matrix)
display(result)
