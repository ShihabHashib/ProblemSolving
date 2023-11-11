import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 349. Intersection of Two Arrays


def intersection(nums1, nums2):
    result = []
    arr1, arr2 = list(set(nums1)), list(set(nums2))

    for i in arr1:
        if i in arr2:
            result.append(i)

    print(result)


# END
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

result = intersection(nums1, nums2)
display(result)
