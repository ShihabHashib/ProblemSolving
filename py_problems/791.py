import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 791. Custom Sort String


def countDigits(order, s):
    result = ""
    dic = {}
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for i in order:
        if i in dic:
            result += i * dic[i]
            dic[i] -= 1 * dic[i]

    for i, value in dic.items():
        if value > 0:
            result += i * value

    return result


# END
order = "kqep"
s = "pekeq"

result = countDigits(order, s)
display(result)
