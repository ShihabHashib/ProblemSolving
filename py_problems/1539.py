import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1539. Kth Missing Positive Number


def findKthPositive(arr, k):
    newArr = []
    for i in range(1, max(arr) + 1 + k):
        if i not in arr:
            newArr.append(i)
    print(newArr)
    return newArr[k - 1]


# END
arr = [1, 2, 3, 4]
k = 2

result = findKthPositive(arr, k)
display(result)
