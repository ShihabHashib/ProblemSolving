import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2469. Convert the Temperature


def convertTemperature(celsius):
    return [celsius + 273.15, celsius * 1.80 + 32.00]


# END
celsius = 36.50
result = convertTemperature(celsius)
display(result)
