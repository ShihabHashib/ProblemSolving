import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2357. Make Array Zero by Subtracting Equal Amounts


def minimumOperations(nums):
    return len(set(nums) - {0})


# END

nums = [1, 5, 0, 3, 5]
result = minimumOperations(nums)
display(result)
