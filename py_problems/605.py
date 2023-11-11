import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 605. Can Place Flowers


def canPlaceFlowers(flowerbed, n):
    if n == 0:
        return True

    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True

    return False


# END
flowerbed = [0, 1, 0, 1, 0, 1, 0, 0]
n = 1

result = canPlaceFlowers(flowerbed, n)
display(result)
