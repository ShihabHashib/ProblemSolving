import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 476. Number Complement


def findComplement(num):
    return int("".join(['1' if char == '0' else '0' for char in str("{0:b}".format(num))]), 2)


# END

num = 1

result = findComplement(num)
display(result)
