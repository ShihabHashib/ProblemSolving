import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1. Two Sum


def twoSum(nums, target):
    store = {}

    for i, j in enumerate(nums):
        com = target - j

        if com in store:
            return [store[com], i]

        store[j] = i


# END
nums = [3, 2, 3]
target = 6

result = twoSum(nums, target)
display(result)
