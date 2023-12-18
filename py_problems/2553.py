import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2553. Separate the Digits in an Array


def separateDigits(nums):
    result = []
    for i in nums:
        temp = []
        while i > 0:
            temp.insert(0, i % 10)
            i = i//10
        result += temp
    return result


# END


nums = [13, 25, 83, 77]
result = separateDigits(nums)
display(result)
