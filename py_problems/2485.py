import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2485. Find the Pivot Integer


def pivotInteger(n):
    num1, num2 = 0, 0

    for i in range(1, n + 1):
        num1 = sum(range(1, i + 1))
        num2 = sum(range(i, n + 1))
        if (num1 == num2):
            return i

    return -1


# END


n = 8
result = pivotInteger(n)
display(result)
