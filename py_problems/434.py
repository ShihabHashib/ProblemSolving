import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 434. Number of Segments in a String


def countSegments(s):
    return len(s.split())


# END
s = "Hello, my name is John"

result = countSegments(s)
display(result)
