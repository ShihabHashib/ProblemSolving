import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2824. Count Pairs Whose Sum is Less than Target


def countPairs(nums, target):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(n):
            lastSum = nums[j] + nums[i]
            if 0 <= i < j < n and lastSum < target:
                count += 1
    return count


# END
nums = [-6, 2, 5, -2, -7, -1, 3]
target = -2

result = countPairs(nums, target)
display(result)
