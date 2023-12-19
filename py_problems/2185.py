import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2185. Counting Words With a Given Prefix


def prefixCount(words, pref):
    count = 0
    for i in words:
        if i.startswith(pref):
            count += 1

    return count


# END


words = ["pay", "attention", "practice", "attend"]
pref = "at"
result = prefixCount(words, pref)
display(result)
