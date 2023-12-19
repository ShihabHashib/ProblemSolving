import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1710. Maximum Units on a Truck


def maximumUnits(boxTypes, truckSize):
    result = 0
    boxTypes.sort(key=lambda x: x[1], reverse=True)

    for i, units in boxTypes:
        while i and truckSize > 0:
            result += units
            i -= 1
            truckSize -= 1

    return result


# END
boxTypes = [[1, 3], [2, 2], [3, 1]]
truckSize = 4

result = maximumUnits(boxTypes, truckSize)
display(result)  # imported from pyscript
