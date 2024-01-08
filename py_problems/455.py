import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 455. Assign Cookies


def findContentChildren(g, s):
    count = 0
    cookies, child, g, s = len(s) - 1,  len(g) - 1, sorted(g), sorted(s)

    while min(cookies, child) >= 0:
        if g[child] <= s[cookies]:
            count += 1
            cookies -= 1

        child -= 1

    return count


# END
g = [1, 2, 3]
s = [1, 1]

result = findContentChildren(g, s)
display(result)
