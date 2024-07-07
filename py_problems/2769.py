import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2769. Find the Maximum Achievable Number


def theMaximumAchievableX(num, t):
    return num + (2 * t)

# END


num = 4
t = 1
result = theMaximumAchievableX(num, t)
display(result)
