import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 941. Valid Mountain Array


def validMountainArray(arr):
    count = len(arr)

    if count < 3:
        return False

    maxValueIndex = arr.index(max(arr))

    if maxValueIndex == 0 or maxValueIndex == count - 1:
        return False

    for i in range(1, maxValueIndex):
        if arr[i] <= arr[i - 1]:
            return False

    for i in range(maxValueIndex + 1, count):
        if arr[i] >= arr[i - 1]:
            return False

    return True


# END

arr = [0, 3, 2, 1]
result = validMountainArray(arr)
display(result)
