'''
Counting Sort is a non-comparison-based sorting algorithm that works 
by counting the number of occurrences of each element and using that information to place the elements in sorted order.
'''

def counting_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    range_of_elements = max_value - min_value + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    for i in range(len(arr)):
        count[arr[i] - min_value] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_value] - 1] = arr[i]
        count[arr[i] - min_value] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]


arr = [1, 3, 5, 6, 0, 2, 8, 4, 9, 7]
counting_sort(arr)
print(arr)