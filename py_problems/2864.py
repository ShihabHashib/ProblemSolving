import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2864. Maximum Odd Binary Number


def maximumOddBinaryNumber(s):
    result = ""
    count0 = s.count("0")
    count1 = s.count("1")

    for i in range(count1 - 1):
        result += '1'

    for i in range(count0):
        result += '0'

    result += '1'

    return result


# END
s = "010"

result = maximumOddBinaryNumber(s)
display(result)
