import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 217. Contains Duplicate


def containsDuplicate(nums):
    arr = []
    for i in nums:
        if i in arr:
            return True
        arr.append(i)
    return False


# END


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
result = containsDuplicate(nums)
display(result)
