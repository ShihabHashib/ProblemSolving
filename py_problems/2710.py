import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2710. Remove Trailing Zeros From a String


def removeTrailingZeros(num):
    while num[-1] == '0':
        num = num[:-1]

    return num


# END
num = "51230100"

result = removeTrailingZeros(num)
display(result)
