import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2652. Sum Multiples


def sumOfMultiples(n):
    count = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            count += i
    return count


# END


n = 9
result = sumOfMultiples(n)
display(result)
