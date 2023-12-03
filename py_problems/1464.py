import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1464. Maximum Product of Two Elements in an Array


def singleNumber(nums):
    nums.sort(reverse=True)
    largest = nums[0]
    secondLargest = nums[1]

    return (largest - 1) * (secondLargest - 1)


# END

nums = [3, 4, 5, 2]
result = singleNumber(nums)
display(result)
