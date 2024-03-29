def quicksort_r(arr,left,right):
    if left < right:   #to check if subarray contains atleast 2 elements
        partition_pos = partition(arr, left, right)
        arr = quicksort_r(arr, left, partition_pos -1) #quicksort on subarray that are less than pivot elements
        arr = quicksort_r(arr, partition_pos + 1, right) #quicksort on subarray that are greater than pivot elements

    return arr

def partition(arr, left, right):
    i = left
    j = right -1 
    pivot =arr[right]
    while i < j:  #condition to check i and j crossing
        while i < right  and arr[i] < pivot:   #moving i to the right
            i += 1
        while j > left and arr[j] >= pivot:  #moving j to the left
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]  #swap
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right],arr[i]
    return i
