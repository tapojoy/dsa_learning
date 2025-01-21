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
