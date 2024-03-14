import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1876. Substrings of Size Three with Distinct Characters


def countGoodSubstrings(s):
    count = 0

    for i in range(len(s) - 2):
        str = set(s[i:i+3])
        if len(str) == 3:
            count += 1

    return count


# END
s = "xzyzaz"

result = countGoodSubstrings(s)
display(result)
