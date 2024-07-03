import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 3110. Score of a String


def scoreOfString(s):
    count  = 0

    for i in range(len(s) - 1):
        count += abs(ord(s[i]) - ord(s[i + 1]))

    return count

# END


s = "hello"
result = scoreOfString(s)
display(result)
