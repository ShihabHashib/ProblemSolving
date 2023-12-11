import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1475. Final Prices With a Special Discount in a Shop


def finalPrices(prices):
    result = []

    for i in range(len(prices)):
        for j in range(1, len(prices)):
            if j > i and prices[j] <= prices[i]:
                result.append(prices[i] - prices[j])
                break
        else:
            result.append(prices[i])

    return result


# END
prices = [8, 4, 6, 2, 3]

result = finalPrices(prices)
display(result)
