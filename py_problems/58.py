import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 58. Length of Last Word


def lengthOfLastWord(s):
    newStr = s.split()
    getLen = len(newStr[-1])
    return getLen


# END
str = "Hello World"

result = lengthOfLastWord(str)
display(result)
