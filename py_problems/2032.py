import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2032. Two Out of Three


def twoOutOfThree(nums1, nums2, nums3):
    return set(nums1) & set(nums2) or set(nums2) & set(nums3) or set(nums1) & set(nums3)

# END


nums1 = [1, 1, 3, 2]
nums2 = [2, 3]
nums3 = [3]
result = twoOutOfThree(nums1, nums2, nums3)
display(result)
