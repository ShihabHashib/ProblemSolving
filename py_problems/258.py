import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 258. Add Digits


def addDigits(num):
    st = str(num)

    while len(st) > 1:
        n = 0
        for i in range(len(st)):
            n += int(st[i])
        st = str(n)

    return int(st)

# END
num = 38

result = addDigits(num)
display(result)
