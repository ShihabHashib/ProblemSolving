import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1748. Sum of Unique Elements


def sumOfUnique(nums):
    result = 0
    for i in nums:
        if nums.count(i) == 1:
            result += i
    return result


# END
nums = [1, 2, 3, 4, 5]

result = sumOfUnique(nums)
display(result)
