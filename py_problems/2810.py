import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2810. Faulty Keyboard


def finalString(s):
    result = ""
    for i in s:
        if i == "i":
            result = result[::-1]
        else:
            result += i
    return result


# END


s = "poiinter"

result = finalString(s)
display(result)
