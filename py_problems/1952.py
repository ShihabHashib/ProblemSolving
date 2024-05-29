import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1952. Three Divisors


def isThree(n):
    count = []
    
    for i in range(1, n + 1):
        if n % i == 0:
            count.append(i)

    return len(count) == 3

# END
n = 4

result = isThree(n)
display(result)
