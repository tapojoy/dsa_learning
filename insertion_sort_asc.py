
a = [2,5,1,7,3]
print(a)

def insertion_sort_asc(array, verbose=False):
    if verbose: print("entering loop\n---")
    for j in range(1, len(array)):
        if verbose: print("current array : " + str(array))
        if verbose: print("ptr j is at " + str(j))
        key = array[j]
        if verbose: print("key = array[j] = array[" + str(j) + "] which is equal to " + str(key))
        i = j - 1
        if verbose: print("i is assigned " + str(i))
        while i > -1 and array[i] > key:
            if verbose: print("->i has not preceeded yet AND array[" + str(i) + "] = " + str(array[i]) + " is greater than key")
            array[i + 1] = array[i]
            if verbose: print("shift right and now array is : " + str(array))
            i = i - 1
            if verbose: print("decrement i and i = " + str(i))
        if verbose: print("->i has either preceeded OR array[i] = " + str(array[i]) + " is NOT greater than key")
        array[i + 1] = key
        if verbose: print("insert here and now array is : " + str(array))
        if verbose: print("move index j\n---")
    if verbose: print("returning array : " + str(array) + "\n---")
    return array

print(insertion_sort_asc(a, True))
