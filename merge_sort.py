def merge(A, p, q, r, lvl, verbose=False):
    L = A[p:q]
    R = A[q:r]
    l_len = q - p
    r_len = r - q
    i = 0
    j = 0
    if verbose: print(" > > merge routine, lvl = " + str(lvl) + ",")
    if verbose: print(" > > p = " + str(p) + ", q = " + str(q) + ", r = " + str(r))
    if verbose: print(" > > L = " + str(L) + ", R = " + str(R))
    while p <= r and i<l_len and j<r_len:
        if L[i] <= R[j]:
            A[p] = L[i]
            i = i + 1
            if verbose: print(" > > i = " + str(i) + ", j = " + str(j) + ", p = " + str(p) + ", A = " + str(A))
        else:
            A[p] = R[j]
            j = j + 1
            if verbose: print(" > > i = " + str(i) + ", j = " + str(j) + ", p = " + str(p) + ", A = " + str(A))
        p = p + 1
    if p!=r:
        if j == r_len:
            while i<l_len:
                A[p] = L[i]
                p += 1
                i += 1
                if verbose: print(" > > i = " + str(i) + ", j = " + str(j) + ", p = " + str(p) + ", A = " + str(A))
        elif i == l_len:
            while j<r_len:
                A[p] = R[j]
                p += 1
                j += 1
                if verbose: print(" > > i = " + str(i) + ", j = " + str(j) + ", p = " + str(p) + ", A = " + str(A))
    return A

def merge_sort(array, p, r, lvl=0, verbose=False):
    if not isinstance(array,list):
        return None
    lvl += 1
    l = r - p
    if l <= 1:
        if verbose: print(" > base condition, p = " + str(p) + ", r = " + str(r) + ", A[p] = " + str(array[p]))
        return array
    else:
        q = p + int(l / 2)

        if verbose: print("lvl = " + str(lvl) + ", induction, p = " + str(p) + ", q = " + str(q) + ", r = " + str(r))
        array = merge_sort(array, p, q, lvl, verbose)

        if verbose: print("lvl = " + str(lvl) + ", induction, p = " + str(p) + ", q = " + str(q) + ", r = " + str(r))
        array = merge_sort(array, q, r, lvl, verbose)

        array = merge(array, p, q, r, lvl, verbose)
        return array
