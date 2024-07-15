import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1356. Sort Integers by The Number of 1 Bits


def sortByBits(arr):
    arr.sort(key = lambda x: (bin(x).count('1'), x))
    return arr


# END
arr = [0,1,2,3,4,5,6,7,8]

result = sortByBits(arr)
display(result)
