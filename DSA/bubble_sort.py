'''
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, 
and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.
'''

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 2, 1, 8, 4]
bubble_sort(arr)
print(arr)  # Output: [1, 2, 4, 5, 8]
