import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 405. Convert a Number to Hexadecimal


def toHex(num):
    if num == 0:
        return '0'

    hex_chars = "0123456789abcdef"
    result = ""

    if num < 0:
        num += 2**32

    while num > 0:
        remainder = num % 16
        result = hex_chars[remainder] + result
        num //= 16

    return result


# END


num = 26
result = toHex(num)
display(result)
