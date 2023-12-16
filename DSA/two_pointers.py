def two_pointers(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return arr[left], arr[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
result = two_pointers(arr, target)
print(f"Pair with sum {target}: {result}")
