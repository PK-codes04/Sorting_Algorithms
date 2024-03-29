def bubble_sort(arr):
    is_sorted = False #to track if array is sorted or not
    while is_sorted == False:
        is_sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swap(i, i+1, arr)
                is_sorted = False
    return arr
def swap(i, j, arr):
    arr[i],arr[j] = arr[j],arr[i]






