import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 500. Keyboard Row


def findWords(words):
    firstRow = 'qwertyuiop'
    secondRow = 'asdfghjkl'
    thirdRow = 'zxcvbnm'

    result = []

    for word in words:
        lowerWord = word.lower()
        firstChar = lowerWord[0]

        if firstChar in firstRow:
            row = firstRow
        elif firstChar in secondRow:
            row = secondRow
        else:
            row = thirdRow

        if all(char in row for char in lowerWord):
            result.append(word)

    return result


# END
words = ["Hello", "Alaska", "Dad", "Peace"]

result = findWords(words)
display(result)
