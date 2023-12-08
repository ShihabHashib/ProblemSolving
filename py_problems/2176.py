import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2176. Count Equal and Divisible Pairs in an Array


def countPairs(nums, k):
    count = 0

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j and nums[i] == nums[j] and (i*j) % k == 0:
                count += 1
    return count


# END
nums = [3, 1, 2, 2, 2, 1, 3]
k = 2

result = countPairs(nums, k)
display(result)
