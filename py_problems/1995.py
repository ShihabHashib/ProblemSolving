from itertools import combinations
import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1995. Count Special Quadruplets


def countQuadruplets(nums):
    return sum([1 for a, b, c, d in combinations(nums, 4) if a + b + c == d])


# END
nums = [1, 2, 3, 6]

result = countQuadruplets(nums)
display(result)
