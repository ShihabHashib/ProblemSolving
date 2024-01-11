import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 415. Add Strings


def addStrings(num1, num2):
    sys.set_int_max_str_digits(10000)
    return str(int(num1) + int(num2))


# END
num1 = "11"
num2 = "123"

result = addStrings(num1, num2)
display(result)
