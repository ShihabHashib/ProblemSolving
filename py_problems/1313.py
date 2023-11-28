import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 1313. Decompress Run-Length Encoded List


def decompressRLElist(nums):
    result = []
    for i in range(0, len(nums), 2):
        f = nums[i]
        v = nums[i+1]
        result += [v] * f
    return result


# END
nums = [1, 2, 3, 4]

result = decompressRLElist(nums)
display(result)
