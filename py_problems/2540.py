import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2540. Minimum Common Value


def getCommon(nums1, nums2):
    i, j = 0, 0

    while i <= len(nums1) and j <= len(nums2):
        if nums1[i] == nums2[j]:
            return nums1[i]
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return -1


    # a, b = set(nums1), set(nums2)
    # c = sorted(list(a & b))
    # return -1 if not len(c) else c[0]
# END
nums1 = [1, 2, 3, 6]
nums2 = [2, 3, 4, 5]
result = getCommon(nums1, nums2)
display(result)
