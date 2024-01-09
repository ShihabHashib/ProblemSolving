import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2053. Kth Distinct String in an Array


def kthDistinct(arr, k):
    newList = []

    for i in arr:
        if arr.count(i) == 1:
            newList.append(i)
    if len(newList) < k:
        return ""
    return newList[k - 1]


# END
arr = ["a", "b", "a"]
k = 3

result = kthDistinct(arr, k)
display(result)
