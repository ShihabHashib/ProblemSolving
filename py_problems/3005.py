import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 3005. Count Elements With Maximum Frequency


def maxFrequencyElements(nums):
    from collections import Counter
    dic = Counter(nums)
    maxNum = max(dic.values())
    return sum(filter(lambda x: x == maxNum, dic.values()))


# END
nums = [1, 2, 2, 3, 1, 4]

result = maxFrequencyElements(nums)
display(result)
