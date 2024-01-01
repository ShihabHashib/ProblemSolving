import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1486. XOR Operation in an Array


def xorOperation(n, start):
    xor = 0
    for i in range(n):
        xor ^= start + 2 * i

    return xor


# END
n = 4
start = 3
result = xorOperation(n, start)
display(result)
