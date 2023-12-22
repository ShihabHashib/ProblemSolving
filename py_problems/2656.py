import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2656. Maximum Sum With Exactly K Elements


def findNumbers(nums):
    maxValue = max(nums)

    for i in range(maxValue+1, maxValue+k):
        maxValue += i

    return maxValue


# END

nums = [1, 2, 3, 4, 5]
k = 3
result = findNumbers(nums)
display(result)
