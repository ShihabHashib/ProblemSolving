import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 643. Maximum Average Subarray I


def findMaxAverage(nums, k):
    result = []
    sortedArr = sorted(nums, key=lambda x: (-abs(x), x))

    for num in sortedArr:
        if not result or num != result[-1]:
            result.append(num)

    total = sum(result[:k])
    return total / k


# END
nums = [1, 0, 1, 4, 2]
k = 4
result = findMaxAverage(nums, k)
display(result)
