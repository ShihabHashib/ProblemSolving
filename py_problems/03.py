import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 3. Longest Substring Without Repeating Characters


def lengthOfLongestSubstring(s):
    count = {}
    l = 0
    length = 0

    for i in range(len(s)):
        temp = s[i]
        if temp in count and count[temp] >= l:
            l = count[temp] + 1
        else:
            length = max(length, i - l + 1)
        count[temp] = i

    return length


# END
s = "abcabcbb"

result = lengthOfLongestSubstring(s)
display(result)
