import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1991. Find the Middle Index in Array


def findMiddleIndex(nums):
    left = 0
    right = sum(nums)

    for i, num in enumerate(nums):
        right -= num
        if right == left:
            return i
        left += num

    return -1


# END
nums = [2, 3, -1, 8, 4]

result = findMiddleIndex(nums)
display(result)
