import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 14. Longest Common Prefix


def longestCommonPrefix(strs):
    if not strs:
        return ""

    strs.sort()
    firstItem = strs[0]
    lastItem = strs[-1]

    i = 0
    while i < len(firstItem) and i < len(lastItem) and firstItem[i] == lastItem[i]:
        i += 1
    return firstItem[:i]


# END
strs = ["dog", "racecar", "car"]

result = longestCommonPrefix(strs)
display(result)
