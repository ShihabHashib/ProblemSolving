import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 00. Test Code


def namef(matrix):
    m, n = len(matrix), len(matrix[0])

    minRow = [min(x) for x in matrix]
    maxCol = max(matrix, key=max)

    print(maxCol)


matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]

result = namef(matrix)
display(result)
