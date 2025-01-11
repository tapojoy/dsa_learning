def merge(A,p,q,r):
    k = p
    l = r
    L = A[p:q+1]
    R = A[q+1:r+1]
    l_len = q + 1 - p # len(L)
    r_len = r - q # len(R)
    i = 0
    j = 0
    print(" i = " + str(i) + ", j = " + str(j) + ", k = " + str(k) + ", A = " + str(A))
    while k <= l and i<l_len and j<r_len:
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
            print(" i = " + str(i) + ", j = " + str(j) + ", k = " + str(k) + ", A = " + str(A))
        else:
            A[k] = R[j]
            j = j + 1
            print(" i = " + str(i) + ", j = " + str(j) + ", k = " + str(k) + ", A = " + str(A))
        k = k + 1
    if k!=l:
        if j == r_len:
            while i<l_len:
                A[k] = L[i]
                k += 1
                i += 1
                print(" i = " + str(i) + ", j = " + str(j) + ", k = " + str(k) + ", A = " + str(A))
        elif i == l_len:
            while j<r_len:
                A[k] = R[j]
                k += 1
                j += 1
                print(" i = " + str(i) + ", j = " + str(j) + ", k = " + str(k) + ", A = " + str(A))
    return A
