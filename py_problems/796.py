import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 796. Rotate String


def rotateString(s, goal):
    s_len = len(s)
    while s_len > 0:
        rotated = s[-1:] + s[:-1]
        s = rotated
        s_len = s_len - 1
        if s == goal:
            return s
    return None
# END


s = "abcde"
goal = "cdeab"

result = rotateString(s, goal)
display(result)
