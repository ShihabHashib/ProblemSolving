import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 119. Pascal's Triangle II


def getRow(rowIndex):
    triAngle = []

    for i in range(rowIndex + 1):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triAngle[i - 1][j-1] + triAngle[i-1][j]
        triAngle.append(row)

    return triAngle[-1]


# END
rowIndex = 3

result = getRow(rowIndex)
display(result)
