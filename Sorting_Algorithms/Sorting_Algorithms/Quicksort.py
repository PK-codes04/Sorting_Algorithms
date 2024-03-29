import time
def partition(arr_test, start, end):
    i = start-1 #left pointer
    pivot = arr_test[(start+end)//2] # pivot
   # print(f"Pivot = {pivot}")
    j = end+1 #right pointer
    while True:
        i+=1
        while (arr_test[i] < pivot):
            i+=1 #move left pointer to right
        j-=1
        while (arr_test[j]> pivot):
            j-=1 #move right pointer to left
        if i>=j:
            return j #stop, pivot moved to its correct position
        arr_test[i], arr_test[j] = arr_test[j], arr_test[i] 
#print(f"Array after partitioning:{arr_test}")
def quickSort(arr_test, start, end):
    if start < end:
        p = partition(arr_test, start, end) # p is pivot, it is now at its correct position
        # sort elements to left and right of pivot separately
        arr_test = quickSort(arr_test, start, p)
        arr_test = quickSort(arr_test, p+1, end)
    return arr_test