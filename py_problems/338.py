import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 338. Counting Bits


def countBits(n):
    total = []
    for i in range(0, n + 1):
        binary = "{0:b}".format(i)
        total.append(binary.count('1'))
    return total


# END
n = 5

result = countBits(n)
display(result)
