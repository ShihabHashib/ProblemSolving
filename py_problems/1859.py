import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1859. Sorting the Sentence


def sortSentence(s):
    result = ""
    sortedArr = [i[-1] + i[:-1] for i in s.split()]
    sortedArr.sort()

    for i in sortedArr:
        result += i[1:] + " "

    return result[:-1]


# END


s = "is2 sentence4 This1 a3"

result = sortSentence(s)
display(result)
