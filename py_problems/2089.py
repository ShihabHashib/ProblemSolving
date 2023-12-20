import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2089. Find Target Indices After Sorting Array


def targetIndices(nums, target):
    indices = []
    nums.sort()

    for i in range(len(nums)):
        if nums[i] == target:
            indices.append(i)

    return indices


# END

nums = [1, 2, 5, 2, 3]
target = 2
result = targetIndices(nums, target)
display(result)
