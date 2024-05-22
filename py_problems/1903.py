import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1903. Largest Odd Number in String


def largestOddNumber(num):
    for n, i in enumerate(num[::-1]):
            if int(i) % 2 != 0:
                return num[:len(num) - n]

    return ""




# END Code

num = "52"

result = largestOddNumber(num)
display(result)
