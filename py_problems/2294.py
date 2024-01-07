import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2294. Partition Array Such That Maximum Difference Is K


def partitionArray(nums, k):
    count, j = 1, 0
    sortedList = sorted(nums)

    for i in range(1, len(nums)):
        if sortedList[i]-sortedList[j] > k:
            count += 1
            j = i

    return count


# END
nums = [3, 6, 1, 2, 5]
k = 2

result = partitionArray(nums, k)
display(result)
