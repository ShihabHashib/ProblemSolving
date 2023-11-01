import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 561. Array Partition


def arrayPairSum(nums):
    nums.sort()
    result = sum(nums[::2])
    return result


# END
nums = [1, 4, 3, 2]

result = arrayPairSum(nums)
display(result)
