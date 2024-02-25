import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1941. Check if All Characters Have Equal Number of Occurrences


def areOccurrencesEqual(s):
    count = []
    for i in set(s):
        count.append(s.count(i))

    if len(set(count)) != 1:
        return False

    return True


# END

s = "aabbccddeded"
result = areOccurrencesEqual(s)
display(result)
