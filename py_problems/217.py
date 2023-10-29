import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 217. Contains Duplicate


def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# END


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
result = containsDuplicate(nums)
display(result)
