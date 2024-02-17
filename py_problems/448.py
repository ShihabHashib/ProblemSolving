import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 448. Find All Numbers Disappeared in an Array


def findDisappearedNumbers(nums):
    return list(set([i for i in range(1, len(nums) + 1)]) - set(nums))


# END
nums = [4, 3, 2, 7, 8, 2, 3, 1]

result = findDisappearedNumbers(nums)
display(result)
