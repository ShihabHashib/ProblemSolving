import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1528. Shuffle String


def restoreString(s, indices):
    suffStr = [''] * len(s)
    for i, j in zip(indices, s):
        suffStr[i] = j

    return ''.join(suffStr)


# END
s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]

result = restoreString(s, indices)
display(result)
