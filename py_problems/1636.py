import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1636. Sort Array by Increasing Frequency


def frequencySort(nums):
    frequencyCount = Counter(nums)
    nums.sort(key=lambda x: (frequencyCount[x], -x))

    return nums


# END
nums = [1, 1, 2, 2, 2, 3]
result = frequencySort(nums)
display(result)
