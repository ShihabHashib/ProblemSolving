import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2006. Count Number of Pairs With Absolute Difference K


def countKDifference(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if abs(nums[i] - nums[j] == k):
                count += 1
    return count


# END
nums = [1, 3]
k = 3

result = countKDifference(nums)
display(result)
