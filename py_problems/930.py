import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 930. Binary Subarrays With Sum


def numSubarraysWithSum(nums, goal):
    count = 0
    sum_count = {0: 1}
    current_sum = 0

    for num in nums:
        current_sum += num
        if current_sum - goal in sum_count:
            count += sum_count[current_sum - goal]
        sum_count[current_sum] = sum_count.get(current_sum, 0) + 1

    return count

    # count = 0
    # for i in range(len(nums)):
    #     sum = 0
    #     for j in range(i, len(nums)):
    #         sum += nums[j]
    #         if (sum == goal):
    #             count += 1

    # return count


# END
nums = [1, 0, 1, 0, 1]
goal = 2

result = numSubarraysWithSum(nums, goal)
display(result)
