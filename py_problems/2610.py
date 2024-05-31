import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2610. Convert an Array Into a 2D Array With Conditions


def findMatrix(nums):
    fre = {}

    for i in nums:
        if i in fre:
            fre[i] += 1
        else:
            fre[i] = 1

    result = [[] for _ in range(max(fre.values()))]

    for num, count in fre.items():
        for i in range(count):
            result[i].append(num)

    return result 


# END
nums = [1,3,4,1,2,3,1]

result = findMatrix(nums)
display(result)
