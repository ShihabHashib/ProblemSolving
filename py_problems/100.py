import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 69. Sqrt(x)


def sqRt(x):
    if x == 0:
        return 0

    left, right = 1, x

    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    return result


# END

x = 4
result = sqRt(x)
display(result)
