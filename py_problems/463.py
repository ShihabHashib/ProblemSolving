import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 463. Island Perimeter


def islandPerimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    total = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                total += 4
                if i > 0 and grid[i - 1][j] == 1:
                    total -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    total -= 2
                    
    return total

# END
grid = [[1,1],[1,1]]

result = islandPerimeter(grid)
display(result)
