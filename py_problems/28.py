import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 28. Find the Index of the First Occurrence in a String

def strStr(haystack, needle):
    if needle == "":
        return 0
    
    for i in range(len(haystack) - len(needle) + 1):
        match = True
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                match = False
                break
        if match:
            return i
    
    return -1
        

        

haystack = "sadbutsad"
needle = "tsa"
result = strStr(haystack, needle)
display(result)