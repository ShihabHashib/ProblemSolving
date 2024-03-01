import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2778. Sum of Squares of Special Elements


def sumOfSquares(nums):
    count = 0
    n = len(nums)

    for i, value in enumerate(nums, 1):
        if n % i == 0:
            count += value**2

    return count


# END
nums = [2, 7, 1, 19, 18, 3]

result = sumOfSquares(nums)
display(result)
