import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1281. Subtract the Product and Sum of Digits of an Integer


def subtractProductAndSum(n):
    product, sum = 1, 1
    for i in str(n):
        product *= int(i)
        sum += int(i)

    return product - sum + 1


# END
n = 4421

result = subtractProductAndSum(n)
display(result)
