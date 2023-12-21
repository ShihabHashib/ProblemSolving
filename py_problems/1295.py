import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1295. Find Numbers with Even Number of Digits


def findNumbers(nums):
    return len([i for i in nums if len(str(i)) % 2 == 0])


# END

nums = [12, 345, 2, 6, 7896]
result = findNumbers(nums)
display(result)
