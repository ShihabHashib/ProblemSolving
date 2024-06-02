import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 78. Subsets


def subsets(nums):
    result = [[]]
    for i in nums:
        result += [subset + [i] for subset in result]
    
    return result


# END
nums = [1,2,3]

result = subsets(nums)
display(result)
