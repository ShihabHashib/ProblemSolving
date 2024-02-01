import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1684. Count the Number of Consistent Strings


def countConsistentStrings(allowed, words):
    return sum(1 for i in words if all(char in allowed for char in i))

    # count = 0

    # for i in words:
    #     for j in i:
    #         if j not in allowed:
    #             count += 1
    #             break

    # return len(words) - count


# END
allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]
result = countConsistentStrings(allowed, words)
display(result)
