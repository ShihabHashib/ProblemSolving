import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 496. Next Greater Element I


def nextGreaterElement(nums1, nums2):
    result = []
    for i in nums1:
        getIndex = nums2.index(i)

        nextGreater = -1
        for j in range(getIndex + 1, len(nums2)):
            if nums2[j] > i:
                nextGreater = nums2[j]
                break

        result.append(nextGreater)

    return result


# END
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

result = nextGreaterElement(nums1, nums2)
display(result)
