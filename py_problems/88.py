import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 88. Merge Sorted Array


def merge(nums1, m, nums2, n):
    nums1[:] = nums1[:m]
    nums1.extend(nums2)
    nums1.sort()


# END
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

result = merge(nums1, m, nums2, n)
display(result)
