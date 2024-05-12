import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 728. Self Dividing Numbers


def selfDividingNumbers(left, right):
    result = []

    for i in range(left, right + 1):
        for j in str(i):
            if j == '0' or i % int(j):
                break
        else:
            result.append(i)

    return result

# END
left = 1
right = 22
result = selfDividingNumbers(left, right)
display(result)
