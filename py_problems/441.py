import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 441. Arranging Coins


def arrangeCoins(n):
    i = 0
    while n >= 0:
        i += 1
        n -= i

    return i - 1


# END
n = 8

result = arrangeCoins(n)
display(result)
