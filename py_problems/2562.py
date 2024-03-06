import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2562. Find the Array Concatenation Value


def findTheArrayConcVal(nums):
    left, right = 0, len(nums) - 1
    count = 0

    while left <= right:

        if left == right:
            count += int(nums[left])
        else:
            count += int(str(nums[left]) + str(nums[right]))

        left += 1
        right -= 1

    return count


# END
nums = [5, 14, 13, 8, 12]
result = findTheArrayConcVal(nums)
display(result)
