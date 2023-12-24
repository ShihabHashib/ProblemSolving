import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2923. Find Champion I


def findChampion(grid):
    winner = 0
    bestTeam = sum(grid[0])

    for i in range(len(grid)):
        if sum(grid[i]) > bestTeam:
            bestTeam = sum(grid[i])
            winner = i
    return winner


# END
grid = [[0, 1], [0, 0]]
result = findChampion(grid)
display(result)
