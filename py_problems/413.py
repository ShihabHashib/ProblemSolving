import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 413. Arithmetic Slices


def numberOfArithmeticSlices(nums):
    count = 0
    current = 0

    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] == nums[i - 1] - nums[i - 2]:
            current += 1
            count += current

        else:
            current = 0

    return count


# END
nums = [1,2,3,4]

result = numberOfArithmeticSlices(nums)
display(result)
