import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1832. Check if the Sentence Is Pangram


def checkIfPangram(sentence):
    return len(set(sentence)) == 26


# END


sentence = "thequickbrownfoxjumpsoverthelazydog"

result = checkIfPangram(sentence)
display(result)
