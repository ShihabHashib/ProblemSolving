import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1460. Make Two Arrays Equal by Reversing Subarrays


def canBeEqual(target, arr):
    return sorted(target) == sorted(arr)


# END

target = [1, 2, 3, 4]
arr = [2, 4, 1, 3]
result = canBeEqual(target, arr)
display(result)
