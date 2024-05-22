import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1323. Maximum 69 Number


def maximum69Number(num):
    return int(str(num).replace('6', '9', 1))

# END
num = 9669

result = maximum69Number(num)
display(result)
