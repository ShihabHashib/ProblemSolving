import sys
sys.path.insert(1, "../../assets/js/pyscript.js")

# Algorithm, Methods and Technique
# Two-Pointer Algorithm


def count_frequency(nums):
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency


nums = [1, 2, 3, 2, 1, 3, 2, 2, 4, 5, 4, 2, 1]
frequency = count_frequency(nums)
result = count_frequency(nums)

display(result)
