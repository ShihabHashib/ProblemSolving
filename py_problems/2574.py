import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2574. Left and Right Sum Differences


def leftRightDifference(nums):
    reverse = nums[::-1]
    leftSumArr = []
    rightSumArr = []
    x = 0
    y = 0

    for i, j in zip(nums, reverse):
        leftSumArr.append(x)
        rightSumArr.append(y)
        x += i
        y += j

    rightSumArr = rightSumArr[::-1]
    return list(map(lambda x, y: abs(x - y), leftSumArr, rightSumArr))


# END
nums = [10, 4, 8, 3]

result = leftRightDifference(nums)
display(result)
