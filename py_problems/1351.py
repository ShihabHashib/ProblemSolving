import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1351. Count Negative Numbers in a Sorted Matrix


def countNegatives(grid):
    flattedList = sum(grid, [])
    return sum(n < 0 for n in flattedList)


# END
grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]

result = countNegatives(grid)
display(result)
