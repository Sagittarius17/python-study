'''
Shell Sort is a variation of insertion sort that allows the exchange of items that are far apart. 
It starts by sorting pairs of elements far apart from each other and gradually reduces the gap between elements to be compared.
'''

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
