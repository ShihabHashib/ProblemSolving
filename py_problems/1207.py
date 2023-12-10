import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1207. Unique Number of Occurrences


def uniqueOccurrences(arr):
    occurrences = {}
    for i in arr:
        occurrences[i] = occurrences.get(i, 0) + 1

    return len(set(occurrences.values())) == len(occurrences)


# END
arr = [1, 2, 2, 1, 1, 3]

result = uniqueOccurrences(arr)
display(result)
