import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 283. Move Zeroes


def moveZeroes(nums):
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(i)


# END
nums = [0, 1, 0, 3, 12]
result = moveZeroes(nums)
display(result)
