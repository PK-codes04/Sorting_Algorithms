import time
def insertion_sort(arr):
    for i in range(1, len(arr)):   #iteration of all unsorted elements
        j = i
        while arr[j - 1] > arr[j] and j > 0:  #checking left neighbour element is greater than currrent element
            arr[j - 1], arr[j] = arr[j], arr[j -1] #swap
            j -= 1
    return arr

