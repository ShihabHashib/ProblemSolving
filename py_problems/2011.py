import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2011. Final Value of Variable After Performing Operations


def finalValueAfterOperations(operations):
    result = 0
    for op in operations:
        if '+' in op:
            result += 1
        elif '-' in op:
            result -= 1
    return result


# END
operations = ["--X", "X++", "X++"]

result = finalValueAfterOperations(operations)
display(result)
