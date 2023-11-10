import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 704. Binary Search


def search(nums, target):
    findIndex = -1
    if target in nums:
        findIndex = nums.index(target)
    return findIndex


# END
nums = [-1, 0, 3, 5, 9, 12]
target = 2

result = search(nums, target)
display(result)
