import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 557. Reverse Words in a String III


def reverseWords(s):
    return ' '.join(i[::-1] for i in s.split())


# END
s = "Let's take LeetCode contest"
result = reverseWords(s)
display(result)
