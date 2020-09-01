def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and key < A[i]:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A


def quick_sort(vett):
    quick_sort2(vett, 0, len(vett) - 1)


def quick_sort2(vett, low, high):
    if low < high:
        q = partition(vett, low, high)  # index of pivot
        quick_sort2(vett, low, q - 1)
        quick_sort2(vett, q + 1, high)


def partition(v, low, high):
    pivot = v[high]
    i = low - 1
    for j in range(low, high):
        if v[j] <= pivot:
            i = i + 1
            v[i], v[j] = v[j], v[i]
    v[i + 1], v[high] = v[high], v[i + 1]

    return i + 1
