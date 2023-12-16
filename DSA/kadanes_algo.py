def kadanes_algorithm(arr):
    max_current = max_global = arr[0]

    for num in arr[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)

    return max_global

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = kadanes_algorithm(arr)
print("Maximum sum subarray:", result)



"""
max_current keeps track of the maximum sum of the subarray ending at the current index.
max_global keeps track of the maximum sum of subarray seen so far.
Iterate through the array, updating max_current and max_global accordingly.
"""