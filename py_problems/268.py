import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 268. Missing Number


def missingNumber(nums):
    maxNum = max(nums) if max(nums) == len(nums) else len(nums) + 1
    nums.sort()
    count = {}

    for i in nums:
        if i not in count:
            count[i] = 1

    for i in range(maxNum):
        if i not in count:
            return i


# END
nums = [0, 1]
result = missingNumber(nums)
display(result)
