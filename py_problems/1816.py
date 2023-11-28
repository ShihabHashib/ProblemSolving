import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1816. Truncate Sentence


def truncateSentence(s, k):
    return " ".join(s.split()[0:k])


# END
s = "Hello how are you Contestant"
k = 4

result = truncateSentence(s, k)
display(result)
