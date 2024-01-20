import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1974. Minimum Time to Type Word Using Special Typewriter


def minTimeToType(word):
    count = len(word)
    curr = 'a'

    for i in word:
        result = (ord(i) - ord(curr)) % 26
        count += min(result, 26 - result)
        curr = i

    return count


# END
word = "bza"

result = minTimeToType(word)
display(result)
