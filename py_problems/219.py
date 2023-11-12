import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 219. Contains Duplicate II


def containsNearbyDuplicate(nums, k):
    box = set()

    for i, j in enumerate(nums):
        if j in box:
            return True

        box.add(j)

        if len(box) > k:
            box.remove(nums[i - k])

    return False


# END


nums = [1, 0, 1, 1]
k = 1

result = containsNearbyDuplicate(nums, k)
display(result)
