import time
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_small_idx = i #index of current small element
        for j in range(i + 1, len(arr)): 
            if arr[j] < arr[cur_small_idx]: #comaprison of element with cur_small_idx
                cur_small_idx = j
        arr[i], arr[cur_small_idx] = arr[cur_small_idx],arr[i] #swapping
    return arr
