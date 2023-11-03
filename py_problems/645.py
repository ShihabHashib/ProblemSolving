import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 645. Set Mismatch


def findErrorNums(nums):
    result = set()
    duplicate = 0
    missing = 0

    for i in nums:
        if i in result:
            duplicate = i
        result.add(i)

    for i in range(1, len(nums) + 1):
        print(i)
        if i not in result:
            missing = i

    return [duplicate, missing]


# END
nums = [1, 2, 2, 4]
result = findErrorNums(nums)
display(result)
