import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1929. Concatenation of Array


def getConcatenation(nums):
    return nums + nums


# END
nums = [1, 2, 1]

result = getConcatenation(nums)
display(result)
