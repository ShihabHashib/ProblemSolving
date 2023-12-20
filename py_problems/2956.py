import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2956. Find Common Elements Between Two Arrays


def findIntersectionValues(nums1, nums2):
    y, z = 0, 0
    numSet1, numSet2 = set(nums1), set(nums2)

    for i in nums1:
        if i in numSet2:
            y += 1

    for i in nums2:
        if i in numSet1:
            z += 1

    return [y, z]


# END


nums1 = [4, 3, 2, 3, 1]
nums2 = [2, 2, 5, 2, 3, 6]
result = findIntersectionValues(nums1, nums2)
display(result)
