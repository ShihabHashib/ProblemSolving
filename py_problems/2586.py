import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2586. Count the Number of Vowel Strings in Range


def vowelStrings(words, left, right):
    count = 0
    vowel =["a","e","i","o","u"]
    for i in words[left: right+1]:
        if i[0] in vowel and i[-1] in vowel:
            count += 1
    return count

# END
words = ["are","amy","u"]
left = 0
right = 2

result = vowelStrings(words, left, right)
display(result)
