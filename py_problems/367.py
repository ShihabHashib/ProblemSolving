import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 367. Valid Perfect Square


def isPerfectSquare(num):
    i = 1
    while i * i < num:
        i += 1
    return i * i == num

    # Another Version
    # result = False
    # sum, i = 0, 1
    # while sum < num:
    #     multi = i * i
    #     sum = multi
    #     if multi == num:
    #         result = True
    #     i = i + 1

    # return result


# END
n = 14

result = isPerfectSquare(n)
display(result)
