import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start Here

arr = [60, 30, 20, 10, 65, 20, 70, 35, 30, 80, 5]

# Get Sum


def getSum(arr):
    total = 0
    for i in arr:
        total += i
    return total

# Get Minimum


def getMin(arr):
    shortest = arr[0]
    for i in arr:
        if i < shortest:
            shortest = i
    return shortest

# Get Maximum


def getMax(arr):
    highest = arr[0]
    for i in arr:
        if i > highest:
            highest = i
    return highest


# Find Index of same item in an array
duplicatesIndex = [i for i, x in enumerate(array) if x == duplicateNum]
