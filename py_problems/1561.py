import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1561. Maximum Number of Coins You Can Get


def maxCoins(piles):

    sortedPiles = sorted(piles)
    totalCoins = sum(sortedPiles[len(piles)//3::2])

    return totalCoins


# END
piles = [2, 4, 5]

result = maxCoins(piles)
display(result)
