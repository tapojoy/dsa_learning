def partition(array, left, right):
    j = left
    x = array[right]
    i = j - 1
    while j < right:
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
        j += 1
    i += 1
    array[i], array[j] = array[j], array[i]
    return i, array

def quick_select(array, left, right, k):
    if right-left == 0:
        return left
    mid, array = partition(array, left, right)
    if k == mid:
        return mid
    elif k < mid:
        return quick_select(array, left, mid-1, k)
    else:
        return quick_select(array, mid+1, right, k-mid)
