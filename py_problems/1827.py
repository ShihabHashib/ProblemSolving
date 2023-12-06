import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1827. Minimum Operations to Make the Array Increasing


def minOperations(nums):
    count = 0
    prev = nums[0]

    for i in range(1, len(nums)):
        if nums[i] <= prev:
            count += prev - nums[i] + 1
            prev += 1
        else:
            prev = nums[i]

    return count


# END
nums = [1, 1, 1]

result = minOperations(nums)
display(result)
