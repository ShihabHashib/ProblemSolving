import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2549. Count Distinct Numbers on Board


def distinctIntegers(n):
    if n == 1:
        return n
    return n - 1


# END
n = 5

result = distinctIntegers(n)
display(result)
