import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 977. Squares of a Sorted Array


def sortedSquares(nums):
    result = []
    for i in nums:
        result.append(abs(i * i))

    return sorted(result)


# END
nums = [-4, -1, 0, 3, 10]

result = sortedSquares(nums)
display(result)
