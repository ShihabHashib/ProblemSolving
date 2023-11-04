import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 643. Maximum Average Subarray I


def findMaxAverage(nums, k):
    maxSum = currentSum = sum(nums[:k])

    for i in range(k, len(nums)):
        currentSum += nums[i] - nums[i - k]
        maxSum = max(maxSum, currentSum)

    return maxSum / k


# END
nums = [1, 0, 1, 4, 2]
k = 4
result = findMaxAverage(nums, k)
display(result)
