import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2221. Find Triangular Sum of an Array


def triangularSum(nums):
    n = len(nums)

    while (n > 0):
        for i in range(n - 1):
            nums[i] = (nums[i] + nums[i+1]) % 10
        n -= 1
    return nums[0]


# END
nums = [1, 2, 3, 4, 5]

result = triangularSum(nums)
display(result)
