import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 191. Number of 1 Bits


def hammingWeight(n):
    binary = "{0:b}".format(n)
    return binary.count('1')


# END

n = 128

result = hammingWeight(n)
display(result)
