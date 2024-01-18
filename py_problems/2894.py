import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2894. Divisible and Non-divisible Sums Difference


def differenceOfSums(n, m):
    list1 = []
    list2 = []
    for i in range(1, n + 1):
        if i % m == 0:
            list2.append(i)
        else:
            list1.append(i)
    return sum(list1) - sum(list2)

# END

n = 10
m = 3

result = differenceOfSums(n, m)
display(result)
