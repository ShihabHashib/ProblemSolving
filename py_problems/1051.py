import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1051. Height Checker


def heightChecker(heights):
    count = 0
    sortedHeight = sorted(heights)

    for i in range(len(heights)):
        if heights[i] != sortedHeight[i]:
            count += 1

    return count


# END

heights = [1, 1, 4, 2, 1, 3]
result = heightChecker(heights)
display(result)
