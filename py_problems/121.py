import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 121. Best Time to Buy and Sell Stock


def maxProfit(prices):
    if not prices:
        return 0

    minPrice = prices[0]
    maxProfit = 0

    for i in prices:
        if i < minPrice:
            minPrice = i
        else:
            maxProfit = max(maxProfit, i - minPrice)

    return maxProfit


# END
prices = [2, 4, 1]

result = maxProfit(prices)
display(result)
