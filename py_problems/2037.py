import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2037. Minimum Number of Moves to Seat Everyone


def minMovesToSeat(seats, students):
    return sum(abs(x - y) for x, y in zip(sorted(seats), sorted(students)))


# END
seats = [3, 1, 5]
students = [2, 7, 4]

result = minMovesToSeat(seats, students)
display(result)
