import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2006. Count Number of Pairs With Absolute Difference K


def countKDifference(nums):
    num_count = {}
    count = 0

    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1

    for num in num_count:
        if k > 0 and num + k in num_count:
            count += min(num_count[num], num_count[num + k])
        elif k == 0 and num_count[num] > 1:
            count += num_count[num] * (num_count[num] - 1) // 2

    return count


# END
nums = [1, 2, 2, 1]
k = 1

result = countKDifference(nums)
display(result)
