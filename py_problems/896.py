import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 896. Monotonic Array


def isMonotonic(nums):
    increasing = decreasing = True

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            decreasing = False
        elif nums[i] < nums[i - 1]:
            increasing = False

    return increasing or decreasing


# END
nums = [6, 5, 4, 4]

result = isMonotonic(nums)
display(result)
