import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 3065. Minimum Operations to Exceed Threshold Value I


def minOperations(nums, k):
    count = 0

    for i in nums:
        if i < k:
            count += 1

    return count



# END
nums = [2,11,10,1,3]
k = 10
result = minOperations(nums, k)
display(result)
