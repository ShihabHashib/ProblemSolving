import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2154. Keep Multiplying Found Values by Two


def findFinalValue(nums, original):
    while original in nums:
        original = 2 * original

    return original


# END
nums = [5, 3, 6, 1, 12]
original = 3
result = findFinalValue(nums, original)
display(result)
