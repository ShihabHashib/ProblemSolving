import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 3005. Count Elements With Maximum Frequency


def maxFrequencyElements(nums):
    countInc = {}

    for i in nums:
        if i in countInc:
            countInc[i] += 1
        else:
            countInc[i] = 1

    maxNum = max(countInc.values())
    return sum(filter(lambda x: x == maxNum, countInc.values()))


# END
nums = [1, 2, 2, 3, 1, 4]

result = maxFrequencyElements(nums)
display(result)
