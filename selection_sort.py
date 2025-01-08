def selection_sort(arr, verbose=False):
    i = 0
    l = len(arr)
    if verbose:
        indices = []
        for k in range(l): indices.append(k)
    while i < l-1:
        key = arr[i]
        cur_least = key
        j = i + 1
        index = i
        if verbose:
            print(">       arr = " + str(arr))
            print(">   indices = " + str(indices))
            print(">         i = " + str(i))
            print(">       key = " + str(key))
            print("> cur_least = " + str(cur_least))
        while j < l:
            if cur_least > arr[j]:
                cur_least = arr[j]
                index = j
            if verbose:
                print(">  >        j = " + str(j))
                print(">  >   arr[j] = " + str(arr[j]))
                print(">  >cur_least = " + str(cur_least))
                print(">  >    index = " + str(index) + str(" | j++"))
            j = j + 1
        arr[i] = cur_least
        arr[index] = key
        if verbose:
            print(">    arr[i] = " + str(arr[i]) + " ( = cur_least)")
            print(">arr[index] = " + str(arr[index]) + " ( = key)")
            print(">sorted arr = " + str(arr) + " ( at i = " + str(i) + " )")
            print(">   indices = " + str(indices) + " | i++")
        i = i + 1
    return arr
