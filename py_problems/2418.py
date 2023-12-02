import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2418. Sort the People


def sortPeople(names, heights):
    sortedPeople = sorted({n: a for n, a in zip(heights, names)}, reverse=True)
    sortedNames = [name for name, _ in sortedPeople]
    return sortedNames


# END
names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]

result = sortPeople(names, heights)
display(result)
