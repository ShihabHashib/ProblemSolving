import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1470. Shuffle the Array


def shuffle(nums, n):
    shuffledArr = []
    for i in range(n):
        shuffledArr.append(nums[i])
        shuffledArr.append(nums[i + n])

    return shuffledArr


# END
nums = [2, 5, 1, 3, 4, 7]
n = 3
result = shuffle(nums, n)
display(result)
