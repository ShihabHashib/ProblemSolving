import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1979. Find Greatest Common Divisor of Array


def findGCD(nums):
    result = 1
    minNum = min(nums)
    maxNum = max(nums)

    for i in range(1, minNum + 1):
        if minNum % i == 0 and maxNum % i == 0:
            result = max(i, result)
    return result


# END
nums = [2, 5, 6, 9, 10]

result = findGCD(nums)
display(result)
