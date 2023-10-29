import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 414. Third Maximum Number


def thirdMax(nums):
    nums = list(set(nums))

    if len(nums) < 3:
        return max(nums)

    nums.sort()
    return nums[-3]


# END
nums = [2, 2, 3, 1]

result = thirdMax(nums)
display(result)
