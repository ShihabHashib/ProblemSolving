import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 215. Kth Largest Element in an Array


def findKthLargest(nums, k):
    return sorted(nums, reverse=True)[k - 1]


# END
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

result = findKthLargest(nums, k)
display(result)
