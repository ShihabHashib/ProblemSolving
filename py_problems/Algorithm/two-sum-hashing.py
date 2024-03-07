import sys
sys.path.insert(1, "../../assets/js/pyscript.js")

# Algorithm, Methods and Technique
# Two sum Hashing Python Dictionary


def two_sum(nums, target):
    num_indices = {}
    result = []

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_indices:
            result.append([num_indices[complement], i])

        num_indices[num] = i

    return result


# Example usage
nums = [4, 5, 6, 7, 15, 31, 55, 12, 2, 54]
target = 38
result = two_sum(nums, target)

display(result)
