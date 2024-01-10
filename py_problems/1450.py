import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1450. Number of Students Doing Homework at a Given Time


def busyStudent(startTime, endTime, queryTime):
    count = 0
    for i in range(len(startTime)):
        if startTime[i] <= queryTime and queryTime <= endTime[i]:
            count += 1
    return count


# END
startTime = [1, 2, 3]
endTime = [3, 2, 7]
queryTime = 4

result = busyStudent(startTime, endTime, queryTime)
display(result)
