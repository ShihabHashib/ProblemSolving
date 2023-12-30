import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1614. Maximum Nesting Depth of the Parentheses


def maxDepth(s):
    count, result = 0, 0

    for i in s:
        if i == "(":
            count += 1
            result = max(result, count)
        elif i == ")":
            count -= 1

    return result


# END
s = "(1+(2*3)+((8)/4))+1"

result = maxDepth(s)
display(result)
