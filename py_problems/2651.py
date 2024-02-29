import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2651. Calculate Delayed Arrival Time


def findDelayedArrivalTime(arrivalTime, delayedTime):
    return (arrivalTime + delayedTime) % 24


# END


arrivalTime = 15
delayedTime = 5

result = findDelayedArrivalTime(arrivalTime, delayedTime)
display(result)
