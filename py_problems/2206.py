import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2206. Divide Array Into Equal Pairs


def divideArray(nums):
    for i in nums:
        if nums.count(i) % 2 == 1:
            return False

    return True


# END
nums = [3, 2, 3, 2, 2, 2]

result = divideArray(nums)
display(result)
