def partition(array, left, right, verbose=False):
    i = left - 1
    x = array[right]
    j = left
    if verbose: print({'i': i, 'j': j, 'array': array})
    while j < right:
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
        if verbose: print({'i': i, 'j': j, 'array': array})
        j += 1
    i += 1
    array[i], array[right] = array[right], array[i]
    if verbose: print({'i': i, 'j': j, 'array': array})
    return i, array

def quick_sort(array, left, right):
    if right - left <= 0:
        return array
    else:
        mid, array = partition(array, left, right)
        array = quick_sort(array, left, mid-1)
        array = quick_sort(array, mid+1, right)
        return array
