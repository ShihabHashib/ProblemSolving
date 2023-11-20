import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1431. Kids With the Greatest Number of Candies


def kidsWithCandies(candies, extraCandies):
    result = []
    greatest = max(candies)
    for i in candies:
        totalCandies = i + extraCandies
        if totalCandies >= greatest:
            result.append(True)
        else:
            result.append(False)
    return result


# END
candies = [2, 3, 5, 1, 3]
extraCandies = 3

result = kidsWithCandies(candies, extraCandies)
display(result)
