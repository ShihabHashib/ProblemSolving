import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 3046. Split the Array


def isPossibleToSplit(nums):
    dictionary = {}

    for i in nums:
        dictionary[i] = dictionary.get(i, 0) + 1

    for i in dictionary.values():
        if i > 2:
            return False

    return True


# END


nums = [1, 1, 2, 2, 3, 4]

result = isPossibleToSplit(nums)
display(result)
