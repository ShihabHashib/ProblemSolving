import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2859. Sum of Values at Indices With K Set Bits


def sumIndicesWithKSetBits(nums, k):
    total = 0
    for i in range(len(nums)):
        binary = "{0:b}".format(i)
        if binary.count('1') == k:
            total += nums[i]
    return total


# END
nums = [5, 10, 1, 5, 2]
k = 1

result = sumIndicesWithKSetBits(nums, k)
display(result)
