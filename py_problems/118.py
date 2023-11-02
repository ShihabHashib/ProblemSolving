import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 118. Pascal's Triangle


def generate(numRows):
    triAngle = []

    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triAngle[i - 1][j-1] + triAngle[i-1][j]
        triAngle.append(row)

    return triAngle


# END
numRows = 5

result = generate(numRows)
display(result)
