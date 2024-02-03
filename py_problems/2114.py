import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2114. Maximum Number of Words Found in Sentences


def mostWordsFound(sentences):
    return max(len(i.split()) for i in sentences)


# END


sentences = ["please wait", "continue to fight", "continue to win"]
result = mostWordsFound(sentences)
display(result)
