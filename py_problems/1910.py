import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1910. Remove All Occurrences of a Substring


def removeOccurrences(s, part):
    while part in s: s = s.replace(part, "", 1)
    return s
        


# END
s = "daabcbaabcbc"
part = "abc"

result = removeOccurrences(s, part)
display(result)
