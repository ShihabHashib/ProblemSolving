import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 709. To Lower Case


def toLowerCase(s):
    result = ""
    for i in s:
        if "A" <= i <= "Z":
            result = result + chr(ord(i) + 32)
        else:
            result = result + i

    return result


# END

s = "Hello"
result = toLowerCase(s)
display(result)
