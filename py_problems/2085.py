import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2085. Count Common Words With One Occurrence


def countWords(words1, words2):
    result = []

    for i in words1:
        if i in words2 and words1.count(i)==1 and words2.count(i)==1:
            result.append(i)

    return len(result)

# END
words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]

result = countWords(words1, words2)
display(result)
