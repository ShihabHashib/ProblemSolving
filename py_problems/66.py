import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 66. Plus One


def plusOne(digits):
    result = 0
    for i in digits:
        result = result * 10 + i

    newValue = result + 1

    intArray = []
    while newValue > 0:
        digit = newValue % 10
        intArray.insert(0, digit)
        newValue //= 10

    return intArray


# END
str = [5, 5, 3]

result = plusOne(str)
display(result)
