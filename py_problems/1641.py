import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1641. Count Sorted Vowel Strings


def countVowelStrings(n):
    return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24


# END
n = 2
result = countVowelStrings(n)
display(result)
