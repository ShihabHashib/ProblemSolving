import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2716. Minimize String Length


def minimizedStringLength(s):
    return len(set(s))


# END
s = "aaabc"

result = minimizedStringLength(s)
display(result)
