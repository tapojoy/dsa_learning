def binary_search(arr, v, left, right, lvl=0, verbose=False):
    lvl += 1
    mid = int((left+right)/2)
    if verbose:
        l = len(arr)
        indices = []
        for i in range(l): indices.append(i)
        print("\n    arr = " + str(arr))
        print("indices = " + str(indices))
        print(
            "lvl = " + str(lvl) +
            ", (left, right) = (" + str(left) + ", " + str(right) + ")" +
            ", mid = " + str(mid) +
            ", arr[mid] = " + str(arr[mid]) +
            ", v = " + str(v)
        )
    if left > right:
        if verbose: print("left > right, value not found")
        return None
    elif v == arr[mid]:
        if verbose: print("value found at index : " + str(mid))
        return mid
    elif v < arr[mid]:
        right = mid - 1
        if verbose: print("right = mid - 1 = " + str(right))
        return binary_search(arr, v, left, right, lvl, verbose)
    else:
        left = mid + 1
        if verbose: print("left = mid + 1 = " + str(left))
        return binary_search(arr, v, left, right, lvl, verbose)
