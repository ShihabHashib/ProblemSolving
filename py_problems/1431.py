import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1431. Kids With the Greatest Number of Candies


def kidsWithCandies(candies, extraCandies):
    result = []
    greatest = max(candies)
    for i in candies:
        if greatest <= i + extraCandies:
            result.append(True)
        else:
            result.append(False)
    return result


# END
candies = [2, 3, 5, 1, 3]
extraCandies = 3

result = kidsWithCandies(candies, extraCandies)
display(result)
