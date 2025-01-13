def binary_search(arr, v, lvl=0, verbose=False):
    lvl += 1
    l = len(arr)
    q = int(l/2)
    res = False
    if verbose:
        indices = []
        for i in range(l): indices.append(i)
        print("    arr = " + str(arr))
        print("indices = " + str(indices))
        print("lvl = " + str(lvl) + ", l = " + str(l) + ", q = " + str(q) + ", arr[q] = " + str(arr[q]) + ", v = " + str(v) + " | ")
    if l == 1:
        if v == arr[q]:
            res = True
        return res
    else:
        if v == arr[q]:
            res = True
        elif v < arr[q]:
            res = binary_search(arr[:q], v, lvl, verbose)
        else:
            res = binary_search(arr[q:l], v, lvl, verbose)
        return res
