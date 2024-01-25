from itertools import combinations
import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2942. Find Words Containing Character


def findWordsContaining(words, x):
    return [i for i, word in enumerate(words) if x in word]


# END
words = ["leet", "code"]
x = "e"

result = findWordsContaining(words, x)
display(result)
