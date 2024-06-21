import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 682. Baseball Game


def calPoints(operations):
    arr = []
 
    for i in operations:
        if i == "C":
            arr.pop()
        elif i == "D":
            arr.append(arr[-1] * 2)
        elif i == "+":
            arr.append(arr[-1] + arr[-2])
        else:
            arr.append(int(i))
    return sum(arr)


# END

ops = ["5","-2","4","C","D","9","+","+"]

result = calPoints(ops)
display(result)
