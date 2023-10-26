import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 504. Base 7


def convertToBase7(num):
    base = 7
    baseResult = []

    if num == 0:
        return "0"

    negative = num < 0
    num = abs(num)

    while num > 0:
        push = num % base
        baseResult.append(push)
        num = num // 7

    if negative:
        baseResult.append("-")

    rs = ''.join(reversed([str(x) for x in baseResult]))
    return rs


# END
num = 100

result = convertToBase7(num)
display(result)
