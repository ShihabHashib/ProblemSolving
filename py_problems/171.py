import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 171. Excel Sheet Column Number


def titleToNumber(columnTitle):
    result = 0

    for i in columnTitle:
        result = result * 26 + ord(i) - ord("A") + 1
    
    return result


# END
columnTitle = "AB"
result = titleToNumber(columnTitle)
display(result)
