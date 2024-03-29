import time
def merge_sort(arr):
    if len(arr)>1:
        left_arr = arr[:len(arr)//2] #begining to middle point
        right_arr = arr[len(arr)//2:] # middle point to end point
        #recursion
        merge_sort(left_arr)
        merge_sort(right_arr)
        #merge
        i = 0  #checks leftmost element of left array
        j = 0  #checks leftmost element of right array
        k = 0  #checks and track index of merged array
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]: #comparsion of left array index i  and right array index j
                arr[k] = left_arr[i]  #saving value of left array index into merged array index
                i += 1
            else:
                arr[k] = right_arr[j] #aving value of right array index into merged array index
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]  #inserting left array elements into mereged array
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j] #inserting right array elements into mereged array
            j += 1
            k += 1
    return arr
