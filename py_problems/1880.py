import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1880. Check if Word Equals Summation of Two Words


def isSumEqual(firstWord, secondWord, targetWord):
    first, second, target = "", "", ""

    for i in firstWord:
        first += str(ord(i) - ord('a'))

    for i in secondWord:
        second += str(ord(i) - ord('a'))

    for i in targetWord:
        target += str(ord(i) - ord('a'))

    return int(first) + int(second) == int(target)


# END

firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"

result = isSumEqual(firstWord, secondWord, targetWord)
display(result)
