import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 905. Sort Array By Parity


def sortArrayByParity(nums):
    even = []
    odd = []
    for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even + odd


# END


nums = [3, 1, 2, 4]
result = sortArrayByParity(nums)
display(result)
