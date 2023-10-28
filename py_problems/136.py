import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 136. Single Number


def singleNumber(nums):
    result = 0
    for i in nums:
        result ^= i
    return result

# END


nums = [2, 2, 1]
result = singleNumber(nums)
display(result)
