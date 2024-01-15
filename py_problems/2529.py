import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2529. Maximum Count of Positive Integer and Negative Integer


def maximumCount(nums):
    return max(len(list(filter(lambda x: x < 0, nums))), len(list(filter(lambda x: x > 0, nums))))


# END
nums = [-2, -1, -1, 1, 2, 3]

result = maximumCount(nums)
display(result)
