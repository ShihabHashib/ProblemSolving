import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 392. Is Subsequence


def isSubsequence(s, t):
    index = 0
    for i in range(len(t)):
        
        if t[i] in s and t[i] == s[index]:
            index += 1
        
    return index == len(s)



# END


s = "abc"
t = "ahbgdc"

result = isSubsequence(s, t)
display(result)
