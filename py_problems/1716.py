import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1716. Calculate Money in Leetcode Bank


def totalMoney(n):
    total, weekInc, single = 0, 0, 1

    for i in range(1, n + 1):
        total += weekInc + single
        single += 1

        if i % 7 == 0:
            weekInc += 1
            single = 1
        
    return total

# END
n = 10

result = totalMoney(n)
display(result)
