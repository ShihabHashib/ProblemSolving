import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2405. Optimal Partition of String


def partitionString(s):
    result, st = 1, ""
    for i in s:
        if i in st:
            result += 1
            st = ""

        st += i
    return result


# END
s = "abacaba"

result = partitionString(s)
display(result)
