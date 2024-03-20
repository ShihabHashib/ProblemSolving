import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2828. Check if a String Is an Acronym of Words


def isAcronym(words, s):
    if len(s) != len(words):
        return False

    for i in range(len(s)):
        if s[i] != words[i][0]:
            return False

    return True


# END


words = ["alice", "bob", "charlie"]
s = "abc"

result = isAcronym(words, s)
display(result)
