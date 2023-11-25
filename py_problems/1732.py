import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1732. Find the Highest Altitude


def largestAltitude(gain):
    temp = 0
    highest = 0
    for i in gain:
        temp += i
        highest = max(temp, highest)
    return highest


# END
gain = [-5, 1, 5, 0, -7]

result = largestAltitude(gain)
display(result)
