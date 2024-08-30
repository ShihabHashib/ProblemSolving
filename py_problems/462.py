import sys
sys.path.insert(1, "../assets/js/pyscript.js")

# ProblemSolving for LeetCode Python Start
# 462. Minimum Moves to Equal Array Elements II


def minMoves2(nums):
        nums.sort()
        median = nums[len(nums) // 2]
        return sum([abs(median - x) for x in nums])

# END
nums = [1,2,3]

result = minMoves2(nums)
display(result)
