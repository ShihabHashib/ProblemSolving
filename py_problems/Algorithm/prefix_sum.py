import sys
sys.path.insert(1, "../../assets/js/pyscript.js")

# Algorithm, Methods and Technique
# Hashing Python Dictionary


def prefix_sum(arr):
    pr_sum = [0] * (len(arr) + 1)
    pr_sum[0] = 0

    for i in range(1, len(arr) + 1):
        pr_sum[i] = arr[i - 1] + pr_sum[i - 1]

    return pr_sum


arr = [1, 2, 3, 4, 5, 6]
result = prefix_sum(arr)

display(result)
