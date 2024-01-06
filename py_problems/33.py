import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 33. Search in Rotated Sorted Array


def search(nums, target):
    if target not in nums:
        return -1
    else:
        return nums.index(target)


# END
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

result = search(nums, target)
display(result)
