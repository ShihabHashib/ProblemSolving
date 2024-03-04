import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 169. Majority Element


def majorityElement(nums):
    nums.sort()
    count = len(nums)
    return nums[count // 2]


# END

nums = [1, 1, 2]
result = majorityElement(nums)
display(result)
