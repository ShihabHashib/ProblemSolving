import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2733. Neither Minimum nor Maximum


def findNonMinOrMax(nums):
    n = len(nums)
    if n < 3:
        return -1

    nums.sort()
    return nums[n // 2]

# END


nums = [3, 2, 1, 4]
result = findNonMinOrMax(nums)
display(result)
