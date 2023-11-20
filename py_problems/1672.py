import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1672. Richest Customer Wealth


def maximumWealth(accounts):
    maxList = set()
    for i in accounts:
        maxList.add(sum(i))

    return max(maxList)


# END
accounts = [[1, 2, 3], [3, 2, 1]]

result = maximumWealth(accounts)
display(result)
