'''
Quick Sort is a divide-and-conquer algorithm that works by selecting a 'pivot' element from the array and partitioning 
the other elements into two sub-arrays according to whether they are less than or greater than the pivot.
'''

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
