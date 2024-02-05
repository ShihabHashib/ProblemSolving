import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2798. Number of Employees Who Met the Target


def numberOfEmployeesWhoMetTarget(hours, target):
    count = 0

    for i in hours:
        if i >= target:
            count += 1

    return count


# END Code

hours = [5, 1, 4, 2, 2]
target = 6

result = numberOfEmployeesWhoMetTarget(hours, target)
display(result)
