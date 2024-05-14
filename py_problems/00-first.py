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

# Converts To Binary
binary = "{0:b}".format(i)


    

# ===================
matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]

# Find Dimention of metrix
m, n = len(matrix), len(matrix[0])  # print: 3 3

# Find minmum in Row
minRow = [min(x) for x in matrix]  # print: [3, 9, 15]

# Find minmum in Row
maxCol = max(matrix, key=max)  # print: [15, 16, 17]
# OR
[max(i) for i in zip(*matrix)]  # print: [15, 16, 17]

total = sum(matrix, []).count(1) # [3, 7, 8, 9, 11, 13, 15, 16, 17]

# ===================
