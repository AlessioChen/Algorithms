import random


def RandomArray(N):
    A = []
    for i in range(0, N):
        A.append(random.randint(1, N))
    return A


def DecreasingArray(N):
    A = []
    for i in range(N - 1, 0, -1):
        A.append(i)
    return A


def SortedArray(N):
    A = []
    for i in range(0, N):
        A.append(i)
    return A
