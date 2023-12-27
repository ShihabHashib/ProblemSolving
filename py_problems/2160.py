import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2160. Minimum Sum of Four Digit Number After Splitting Digits


def minimumSum(num):
    sortedNum = sorted(str(num))
    return int(sortedNum[0] + sortedNum[2]) + int(sortedNum[1] + sortedNum[3])


# END
num = 2932
result = minimumSum(num)
display(result)
