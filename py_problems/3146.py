import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 3146. Permutation Difference between Two Strings


def findPermutationDifference(s, t):
    count  = 0

    for i in set(s):
        count += abs(s.index(i) - t.index(i))

    return count

# END


s = "abc"
t = "bac"
result = findPermutationDifference(s, t)
display(result)
