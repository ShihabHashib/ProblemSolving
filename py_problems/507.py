import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 507. Perfect Number


def checkPerfectNumber(num):
    if num == 1:
        return False

    total = 1

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            total += i + num // i
        i += 1

    return total == num


# END
num = 2016

result = checkPerfectNumber(num)
display(result)
