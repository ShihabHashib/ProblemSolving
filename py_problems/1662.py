import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1662. Check If Two String Arrays are Equivalent


def arrayStringsAreEqual(word1, word2):
    word1 = ''.join(word1)
    word2 = ''.join(word2)
    return word1 == word2


# END
word1 = ["a", "cb"]
word2 = ["ab", "c"]

result = arrayStringsAreEqual(word1, word2)
display(result)
