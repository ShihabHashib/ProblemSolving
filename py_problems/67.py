import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 67. Add Binary


def addBinary(a, b):
    result = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1

    while i >= 0 or j >= 0 or carry:
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0

        bit_sum = bit_a + bit_b + carry
        carry = (bit_sum // 2)

        result.append(str(bit_sum % 2))

        i, j = i - 1, j - 1

    return "".join(result[::-1])


# END


a = "1010"
b = "1011"

binarySum = addBinary(a, b)
display(binarySum)
