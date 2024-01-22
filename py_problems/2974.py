import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2974. Minimum Number Game


def numberGame(nums):
    nums = sorted(nums)

    for i in range(0, len(nums), 2):
        nums[i] , nums[i +1] = nums[i + 1], nums[i]

    return nums

# END


nums = [5,4,2,3]
result = numberGame(nums)
display(result)
