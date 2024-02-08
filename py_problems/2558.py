import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2558. Take Gifts From the Richest Pile


def pickGifts(gifts, k):
    while k > 0:
        k -= 1
        max_gift = max(gifts)
        max_index = gifts.index(max_gift)
        gifts[max_index] = int(max_gift ** 0.5)
    return sum(gifts)


# END Code

gifts = [25, 64, 9, 4, 100]
k = 4

result = pickGifts(gifts, k)
display(result)
