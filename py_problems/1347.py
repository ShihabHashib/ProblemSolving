import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1347. Minimum Number of Steps to Make Two Strings Anagram


def minSteps(s, t):
    freq = [0] * 26
    
    for i in s:
        freq[ord(i) - ord('a')] += 1
    
    for i in t:
        freq[ord(i) - ord('a')] -= 1
    
    steps = sum(abs(count) for count in freq) // 2
    
    return steps


# END

s = "bab"
t = "aba"

result = minSteps(s, t)
display(result)
