import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1750. Minimum Length of String After Deleting Similar Ends


def minimumLength(s):
    left = 0
    right = len(s) - 1

    while left < right and s[left] == s[right]:
        temp = s[left]

        while left <= right and s[left] == temp:
            left += 1

        while right > left and s[right] == temp:
            right -= 1

    return right - left + 1

# END


s = "aabccabba"
result = minimumLength(s)
display(result)
