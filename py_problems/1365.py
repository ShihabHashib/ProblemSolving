import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1365. How Many Numbers Are Smaller Than the Current Number


def smallerNumbersThanCurrent(nums):
    result = []
    n = range(len(nums))
    for i in n:
        count = 0
        for j in n:
            if j != i and nums[j] < nums[i]:
                count += 1
        result.append(count)
    return result


# END
nums = [8, 1, 2, 2, 3]

result = smallerNumbersThanCurrent(nums)
display(result)
