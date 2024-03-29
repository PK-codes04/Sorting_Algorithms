def max_heap(arr,n,idx): #idx is current index

    largest = idx
    left = 2*idx + 1   #left node index
    right =2*idx + 2   #right node index
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]: 
        largest = right
    if largest != idx :
        arr[largest], arr[idx] =arr[idx], arr[largest]  #swapping
        max_heap(arr,n,largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 -1, -1,-1):  #last non leaf element to index 0
        max_heap(arr,n,i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heap(arr,i,0)

    return arr

