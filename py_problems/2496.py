import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2496. Maximum Value of a String in an Array


def maximumValue(strs):
    maxLen = 0
    for i in strs:
        if i.isdigit():
            temp = int(i)
        else:
            temp = len(i)

        if temp > maxLen:
            maxLen = temp

    return maxLen


# END
strs = ["1", "01", "001", "0001"]

result = maximumValue(strs)
display(result)
