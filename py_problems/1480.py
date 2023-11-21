import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1480. Running Sum of 1d Array


def runningSum(nums):
    total = 0
    result = []
    for i in nums:
        total += i
        result.append(total)
    return result


# END
nums = [1, 2, 3, 4]

result = runningSum(nums)
display(result)
