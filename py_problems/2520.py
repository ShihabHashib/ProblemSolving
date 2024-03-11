import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2520. Count the Digits That Divide a Number


def countDigits(num):
    count = 0
    for i in str(num):
        if num % int(i) == 0:
            count += 1
    return count


# END
num = 1248

result = countDigits(num)
display(result)
