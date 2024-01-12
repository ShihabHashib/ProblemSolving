import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 521. Longest Uncommon Subsequence I


def findLUSlength(a, b):
    if a == b:
        return -1
    else:
        return max(len(a), len(b))


# END
a = "aba"
b = "cdc"

result = findLUSlength(a, b)
display(result)
