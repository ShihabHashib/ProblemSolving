import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1920. Build Array from Permutation


def buildArray(nums):
    newArr = []
    for i in range(len(nums)):
        newArr.append(nums[nums[i]])
    return newArr


# END
nums = [0, 2, 1, 5, 3, 4]

result = buildArray(nums)
display(result)
