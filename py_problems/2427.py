import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2427. Number of Common Factors


def commonFactors(a, b):
    count = 0

    for i in range(1, min(a, b) + 1):
        if a % i == b % i == 0:
            count += 1

    return count


# END
a = 12
b = 6
result = commonFactors(a, b)
display(result)
