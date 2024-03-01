import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2744. Find Maximum Number of String Pairs


def maximumNumberOfStringPairs(words):
    count = 0
    revStr = set()

    for i in words:
        if i in revStr:
            count += 1
        else:
            revStr.add(i[::-1])
    return count


# END
words = ["cd", "ac", "dc", "ca", "zz"]

result = maximumNumberOfStringPairs(words)
display(result)
