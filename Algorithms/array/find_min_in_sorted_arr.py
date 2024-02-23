def findMin(rotated_sorted_array):
    start, end = 0, len(rotated_sorted_array)-1
    curr_min = float("inf")
    while start < end:
        mid = (start+end)//2
        curr_min = min(curr_min, rotated_sorted_array[mid])
        
        if rotated_sorted_array[mid] > rotated_sorted_array[end]:
            start = mid + 1
        else:
            end = mid - 1
    return min(curr_min, rotated_sorted_array[start])