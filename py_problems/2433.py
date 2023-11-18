import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2433. Find The Original Array of Prefix Xor


def findArray(pref):
    return [pref[0]]+[(pref[i-1] ^ pref[i]) for i in range(1, len(pref))]


# END
pref = [5, 2, 0, 3, 1]

result = findArray(pref)
display(result)
