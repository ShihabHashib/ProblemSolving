import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 520. Detect Capital


def detectCapitalUse(word):
    return word.istitle() or word.isupper() or word.islower()

# END


word = "USA"
result = detectCapitalUse(word)
display(result)
