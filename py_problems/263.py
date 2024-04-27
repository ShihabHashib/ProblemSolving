import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 263. Ugly Number


def isUgly(n):
    if n < 1: 
        return False

    for i in [2, 3, 5]:
        while n % i == 0:
            n //= i

    return n == 1


# END
n = 6

result = isUgly(n)
display(result)
