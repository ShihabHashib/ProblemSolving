import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 2215. Find the Difference of Two Arrays


def findDifference(nums1, nums2):    
    set1, set2 = set(nums1), set(nums2)
    result1, result2 = list(set1 - set2), list(set2 - set1)
    return [result1, result2]




# END
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

result = findDifference(nums1, nums2)
display(result)
