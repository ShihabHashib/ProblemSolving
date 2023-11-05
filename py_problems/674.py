import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 674. Longest Continuous Increasing Subsequence


def findLengthOfLCIS(nums):
    maxCount = count = 1

    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            count += 1
            maxCount = max(maxCount, count)
        else:
            count = 1

    return maxCount


# END
nums = [1, 3, 5, 4, 7]

result = findLengthOfLCIS(nums)
display(result)
