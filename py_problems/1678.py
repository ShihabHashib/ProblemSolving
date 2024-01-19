import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1678. Goal Parser Interpretation


def interpret(command):
    return command.replace('()', 'o').replace('(al)', 'al')


# END


command = "G()(al)"
result = interpret(command)
display(result)
