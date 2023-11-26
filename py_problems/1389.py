import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1389. Create Target Array in the Given Order


def createTargetArray(nums, index):
    target = []
    for i, j in zip(nums, index):
        target.insert(j, i)

    return target


# END
nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]

result = createTargetArray(nums, index)
display(result)
