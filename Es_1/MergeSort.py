import sys


def MergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)


def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    # Generate L[0...n1] and R[0...n2]
    L = []
    for i in range(0, n1):
        L.append(A[p + i])
    R = []
    for j in range(0, n2):
        R.append(A[q + j + 1])
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
