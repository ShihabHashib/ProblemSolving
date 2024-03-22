import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 326. Power of Three


def isPowerOfThree(n):
    return (n > 0) and 1162261467 % n == 0

# END


n = 27
result = isPowerOfThree(n)
display(result)
