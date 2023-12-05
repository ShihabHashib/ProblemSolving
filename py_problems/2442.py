import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2442. Count Number of Distinct Integers After Reverse Operations


def countDistinctIntegers(nums):
    uniqNum = set()

    for num in nums:
        uniqNum.add(num)
        x, y = num, 0
        while x:
            y = y * 10 + (x % 10)
            x //= 10
        uniqNum.add(y)
    return len(uniqNum)


# END
nums = [1, 13, 10, 12, 31]

result = countDistinctIntegers(nums)
display(result)
