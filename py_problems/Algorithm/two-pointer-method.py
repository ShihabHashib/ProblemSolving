import sys
sys.path.insert(1, "../../assets/js/pyscript.js")

# Algorithm, Methods and Technique
# Two-Pointer Algorithm


def TwoPointer(arr, target_sum):
    arr.sort()
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [arr[left], arr[right]]
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1

    return []


# END
arr = [4, 5, 6, 7, 15, 31, 55, 12, 2, 54]
target_sum = 38
result = TwoPointer(arr, target_sum)
display(result)
