import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1768. Merge Strings Alternately


def mergeAlternately(word1, word2):
    text, i = "", 0

    while i < len(word1) or i < len(word2):
        if i < len(word1):
            text += word1[i]
        if i < len(word2):
            text += word2[i]
        i += 1

    return text

# END


word1 = "abc"
word2 = "pqr"

result = mergeAlternately(word1, word2)
display(result)
