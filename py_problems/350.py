import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 350. Intersection of Two Arrays II


def intersect(nums1, nums2):
    result = []
    count = {}

    for i in nums1:
        count[i] = count.get(i, 0) + 1

    for i in nums2:
        if i in count and count[i] > 0:
            result.append(i)
            count[i] -= 1

    return result


# END

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = intersect(nums1, nums2)
display(result)
