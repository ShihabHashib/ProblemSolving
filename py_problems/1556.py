import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1556. Thousand Separator


def thousandSeparator(n):
        return f"{n:,}".replace(",", ".")

# END
n = 1234

result = thousandSeparator(n)
display(result)
