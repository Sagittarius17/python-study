'''
Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure to build a max-heap or a min-heap. 
It then repeatedly extracts the root element (which is the maximum or minimum, depending on the heap type) and reconstructs the heap.
'''

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
arr = [2, 6, 7, 1, 9, 3, 5, 8, 4]
heap_sort(arr)
print(arr)