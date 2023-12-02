import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1534. Count Good Triplets


def countGoodTriplets(arr, a, b, c):
    count = 0

    for i, x in enumerate(arr[:-2]):
        for j, y in enumerate(arr[i + 1: -1], start=i + 1):
            for z in arr[j + 1:]:
                if (
                    abs(x - y) <= a
                    and abs(y - z) <= b
                    and abs(x - z) <= c
                ):
                    count += 1
    return count


# END
arr = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3

result = countGoodTriplets(arr, a, b, c)
display(result)
