def dutch_flag_algorithm(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

# Example usage:
arr = [2, 0, 1, 2, 1, 0]
dutch_flag_algorithm(arr)
print("Dutch National Flag Algorithm Result:", arr)


"""

The Dutch National Flag algorithm, also known as three-way partitioning, was proposed by Edsger Dijkstra. 
It is a sorting algorithm that separates an array containing three different values (usually 0, 1, and 2) into three sections.

The algorithm maintains three pointers:

Low (L): Points to the beginning of the array where 0s are placed.
Mid (M): Scans the array.
High (H): Points to the end of the array where 2s are placed.
The idea is to iterate through the array and swap elements to ensure that 0s are on the left, 1s in the middle, 
and 2s on the right. The algorithm works in a single pass through the array.
"""