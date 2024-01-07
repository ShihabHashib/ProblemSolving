import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2023. Number of Pairs of Strings With Concatenation Equal to Target


def findKthLargest(nums, target):
    count = 0
    n = range(len(nums))

    for i in n:
        for j in n:
            if nums[i] + nums[j] == target and i != j:
                count += 1
    return count


# END
nums = ["777", "7", "77", "77"]
target = "7777"

result = findKthLargest(nums, target)
display(result)
