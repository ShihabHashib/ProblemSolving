import sys
sys.path.insert(1, "../../assets/js/pyscript.js")

# Algorithm, Methods and Technique
# Sliding Window Algorithm


def maxValue(nums, k):
    total = sum(nums[:k])
    maxTotal = total

    for i in range(len(nums) - k):
        total = total - nums[i] + nums[i + k]
        maxTotal = max(total, maxTotal)

    return maxTotal


# Example usage
nums = [4, 5, 6, 7, 15, 31, 55, 12, 2, 54, 4, 6]
k = 4
result = maxValue(nums, k)

display(result)
