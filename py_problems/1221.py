import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1221. Split a String in Balanced Strings


def balancedStringSplit(s):
    m = c = 0
    for i in s:
        if i == 'L': c += 1
        if i == 'R': c -= 1
        if c == 0: m += 1
    return m

# END

s = "RLRRLLRLRL"
result = balancedStringSplit(s)
display(result)
