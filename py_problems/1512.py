import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1512. Number of Good Pairs


def numIdenticalPairs(nums):
    arr = {}

    for a in nums:
        arr[a] = arr.get(a, 0) + 1

    ans = 0
    for count in arr.values():
        if count >= 2:
            ans += (count * (count - 1)) // 2

    return ans

    # count = 0
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if (i < j) and nums[i] == nums[j]:
    #             count += 1

    # return count


# END
nums = [1, 2, 3, 1, 1, 3]
result = numIdenticalPairs(nums)
display(result)
