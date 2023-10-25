import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 70. Climbing Stairs


def climbStairs(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b


# END
str = 4

result = climbStairs(str)
display(result)
