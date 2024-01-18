import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2413. Smallest Even Multiple


def smallestEvenMultiple(n):   
    if n % 2 == 0: 
        return n
    else:
        return n * 2
    




# END
n = 7

result = smallestEvenMultiple(n)
display(result)
